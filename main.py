from flask import Flask, render_template, request, jsonify
import os
import asyncio

app = Flask(__name__)

# Define the directory where your scripts are located
SCRIPTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'scripts')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scripts/<script_name>', methods=['POST'])
def run_script(script_name):
    script_path = os.path.join(SCRIPTS_DIR, script_name)
    
    # Check if the requested script exists
    if not os.path.exists(script_path):
        return jsonify({'error': 'Script not found'}), 404
    
    # Execute the script
    try:
        # Execute the python script using asyncio subprocess
        asyncio.run(execute_python_script(script_path))
        return jsonify({'message': 'Script executed successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

async def execute_python_script(script_path):
    # Run the python script using subprocess
    os.system(f"python {script_path}")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
