"""
The fast-api server providing the worker's rest api
"""

# endpoints:
#   [put] submit(job_id: str, job_name: str/enum, job_params: dict[str, Any]) -> Ok
#   [get] results(job_id: str, page: int) -> DataBlock
#      ↑ used by either web_ui to get results, or by other worker to obtain inputs for itself
#   [post] read_from(hostname: str, job_id: str) -> Ok
#      ↑ issued by controller so that this worker can obtain its inputs via `hostname::results(job_id)` call
