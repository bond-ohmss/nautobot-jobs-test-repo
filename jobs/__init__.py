from nautobot.apps.jobs import register_jobs
from .hello_jobs_day18 import HelloJobDay18
from .day21_jobs_upload import FileUpload
from .day22_process_csv_files import FileUpload_2


register_jobs(HelloJobDay18, 
              FileUpload,
              FileUpload_2)


