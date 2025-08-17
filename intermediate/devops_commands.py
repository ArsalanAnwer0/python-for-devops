import subprocess

def execute_command(command):
    try:
        process = subprocess.run(command,
                                 shell=True,
                                 check=True,
                                 stdin=subprocess.PIPE,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE
                                 )
        
        return process.stdout.decode()
    except subprocess.CalledProcessError as e:
        error_msg = f"Command failed with exit code {e.returncode}"
        if e.stderr:
            error_msg += f"\nError: {e.stderr.decode()}"
        return error_msg
    except Exception as e:
        return f"An error occurred: {str(e)}"

print(execute_command("docker images"))