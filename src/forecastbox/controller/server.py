"""
The fast-api server providing the controller's rest api
"""

# endpoints:
#   /jobs
#   [put] submit(job_name: str/enum, job_params: dict[str, Any]) -> JobId
#   [get] status(job_id: JobId) -> JobStatus
#     ↑ does not retrieve the result itself. Instead, JobStatus contains optional url where results can be retrieved from
#   /workers
#   [put] register(hostname: str) -> WorkerId
#   [post] update(worker_id: WorkerId, job_id: JobId, job_status: JobStatus) -> Ok
