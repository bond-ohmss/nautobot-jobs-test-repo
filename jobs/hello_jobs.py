from nautobot.apps.jobs import Job, register_jobs

class HelloJobs(Job):

    class Meta: 
        name = "Hello Jobs from Git Repo"

    def run(self):
        self.logger.debug("This is from the Git repo.")

register_jobs(
    HelloJobs,
)

