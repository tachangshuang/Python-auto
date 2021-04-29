# import jenkins
# from pytest_metadata.ci import jenkins
import jenkins

print(jenkins.Jenkins.jobs_count('1'))

server = jenkins.Jenkins('http://192.168.11.176:8882/')
print(server.jobs_count())


