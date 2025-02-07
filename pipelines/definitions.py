import os

from dagster import Definitions, multiprocess_executor
from dagster_k8s import k8s_job_executor

from job_serial import schedule_serial_op, serial
from job_parellel import schedule_parallel_op, parallel
from job_asset_serial import schedule_asset_serial, asset_serial, jas_generate_numbers, jas_filter_even_numbers, jas_sum_numbers, jas_multiply_result
from job_asset_parallel import schedule_asset_parallel, asset_parallel, jap_generate_numbers, jap_filter_even_numbers, jap_filter_odd_numbers, jap_sum_even_numbers, jap_sum_odd_numbers, jap_total_sum

executor_type = os.getenv('DAGSTER_EXECUTOR_TYPE', 'multiprocess')

if executor_type == 'k8s':
    selected_executor = k8s_job_executor
else:
    selected_executor = multiprocess_executor

defs = Definitions(
    assets=[jas_generate_numbers, jas_filter_even_numbers, jas_sum_numbers, jas_multiply_result, jap_generate_numbers, jap_filter_even_numbers, jap_filter_odd_numbers, jap_sum_even_numbers, jap_sum_odd_numbers, jap_total_sum],
    schedules=[schedule_serial_op, schedule_parallel_op, schedule_asset_serial, schedule_asset_parallel],
    jobs=[serial, parallel, asset_serial, asset_parallel],
    executor=selected_executor
)