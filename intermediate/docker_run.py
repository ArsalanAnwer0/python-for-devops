from devops_commands import execute_command

def docker_run():
    print(execute_command("docker run hello-world"))
    
docker_run()