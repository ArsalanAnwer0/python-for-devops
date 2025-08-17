from flask import Flask, jsonify, render_template
import psutil

app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify({"message": "Hi, The server is up and running!"})

@app.route("/cpu")
def monitor_cpu():
    # System wide CPU usage 
    cpu_percent = psutil.cpu_percent(interval=1)
    return jsonify({"system_cpu_utilization": f"{cpu_percent}%"})

@app.route("/process-cpu")
def monitor_process_cpu():
    # Current process CPU + memory usage
    p = psutil.Process()
    cpu_percent = p.cpu_percent(interval=1)
    mem_percent = p.memory_percent() 
    return jsonify({
        "process_cpu_utilization": f"{cpu_percent}%",
        "process_memory_utilization": f"{mem_percent}%"
    })

@app.route("/dashboard")
def dashboard():
    try:
        cpu_percent = psutil.cpu_percent(interval=1)
        mem_percent = psutil.virtual_memory().percent
        return render_template("index.html", 
                             cpu_percent=cpu_percent, 
                             mem_percent=mem_percent)
    except Exception as e:
        return render_template("index.html", 
                             cpu_percent=0, 
                             mem_percent=0, 
                             message=f"Error: {str(e)}")

if __name__ == "__main__":
    print("This will run only if I execute app.py")
    app.run(debug=True)