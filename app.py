import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

load_dotenv()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static"),
    static_url_path="/static"
)

from graph import nexus_graph
app = Flask(__name__)


# Dashboard
@app.route("/")
def home():
    return render_template("index.html")



@app.route("/api/run", methods=["POST"])
def run_task():
    try:
        data = request.get_json(silent=True) or {}
        task = data.get("task", "").strip()

        if not task:
            return jsonify({
                "success": False,
                "error": "Task is empty."
            }), 400

        print("\nNEXUSAI TASK RECEIVED:", task)
        print("Starting LangGraph workflow...")

        result = nexus_graph.invoke({
            "task": task,
            "category": "",
            "research": "",
            "code": "",
            "review": "",
            "final": ""
        })

        print("NEXUSAI WORKFLOW COMPLETED!")

        return jsonify({
            "success": True,
            "category": result.get("category", ""),
            "research": result.get("research", ""),
            "code": result.get("code", ""),
            "review": result.get("review", ""),
            "final": result.get("final", "")
        })

    except Exception as error:
        print("NEXUSAI BACKEND ERROR:", repr(error))

        return jsonify({
            "success": False,
            "error": str(error)
        }), 500


        print("NexusAI Task Started")
        print("Task:", task)

        # Execute LangGraph
        result = nexus_graph.invoke({
            "task": task,
            "category": "",
            "research": "",
            "code": "",
            "review": "",
            "final": ""

        })

        print("\nNexusAI Task Completed!")
        return jsonify({
            "success": True,
            "category": result.get("category", ""),
            "research": result.get("research", ""),
            "code": result.get("code", ""),
            "review": result.get("review", ""),
            "final": result.get("final", "")
        })
    except Exception as error:
        print("\nNEXUSAI ERROR:", repr(error))
        return jsonify({
            "success": False,
            "error": str(error)
        }), 500


# Start Server
if __name__ == "__main__":
    print("   NEXUSAI SERVER STARTING")
    app.run(host="127.0.0.1", port=5000, debug=True)
