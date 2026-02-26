# retrieve the required librarues
from fastapi import FastAPI, Form, HTTPException
from security.guardrails import AISecurityManager # security system file
from core.robot_agent import AutonomousRobot # the simulation tool
from core.ros2_sim import move_robot_arm_ros
from langchain.tools import Tool # convert a python function to a tool
import uvicorn # open fastapi
import threading # we run the server in a seoarate thread


app = FastAPI(title="Secure Embodied AI Controller")
security = AISecurityManager() # creating a security layer

# defination of the tool
tools = [
    Tool(name="RobotMove", func=move_robot_arm_ros, description="Move the robot arm via ROS2 Simulation")
]
# creating agent
robot = AutonomousRobot(tools).create_executor()

# creating path
@app.post("/execute")

async def execute_command(command: str = Form(...)):
    # creating security layer
    is_safe, message = security.scan_query(command)
    if not is_safe: 
        raise HTTPException(status_code=403, detail=message)
    try:
        #  agent execution
        raw_result = robot.invoke({"input": command})
        
        # save user commands in chroma
        robot.memory.add_texts([command])

        #security the outputs
        safe_result = security.sanitize_output(raw_result["output"])
        return {"status": "success", "result": safe_result}
    except Exception as e:
        return {"status": "error", "detail": str(e)}

# play to server
if __name__ == "__main__":  uvicorn.run("main.py", host="127.0.0.1", port=8000, reload=True)