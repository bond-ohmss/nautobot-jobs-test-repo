from nautobot.apps.jobs import Job

class HelloJobDay18(Job):
    class Meta:
        name = "Hello Job (Day 18)"  # unique display name

    def run(self):
        self.logger.debug("This is from the Git repo.")
        self.logger.info("Hello from Day 18")


