from dagster import op

@op(description="Generate a list of numbers from 1 to 10",
    tags={
        "domain": "numbers",
        "dagster-k8s/config": {
            "container_config": {
                "resources": {
                    "requests": {"cpu": "250m", "memory": "256Mi"},
                }
            },
        }
    })
def generate_numbers():
    return list(range(1, 11))

@op(description="Filter even numbers from the list",
    tags={
        "domain": "numbers",
        "dagster-k8s/config": {
            "container_config": {
                "resources": {
                    "requests": {"cpu": "250m", "memory": "256Mi"},
                }
            },
        }
    })
def filter_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

@op(description="Filter odd numbers from the list",
    tags={
        "domain": "numbers",
        "dagster-k8s/config": {
            "container_config": {
                "resources": {
                    "requests": {"cpu": "250m", "memory": "256Mi"},
                }
            },
        }
    })
def filter_odd_numbers(numbers):
    return [num for num in numbers if num % 2 != 0]

@op(description="Calculate the sum of the given list of even numbers",
    tags={
        "domain": "numbers",
        "dagster-k8s/config": {
            "container_config": {
                "resources": {
                    "requests": {"cpu": "250m", "memory": "256Mi"},
                }
            },
        }
    })
def sum_even_numbers(numbers):
    return sum(numbers)

@op(description="Calculate the sum of the given list of odd numbers",
    tags={
        "domain": "numbers",
        "dagster-k8s/config": {
            "container_config": {
                "resources": {
                    "requests": {"cpu": "250m", "memory": "256Mi"},
                }
            },
        }
    })
def sum_odd_numbers(numbers):
    return sum(numbers)

@op(description="Sum two numbers",
    tags={
        "domain": "numbers",
        "dagster-k8s/config": {
            "container_config": {
                "resources": {
                    "requests": {"cpu": "250m", "memory": "256Mi"},
                }
            },
        }
    })
def sum_two_numbers(first_number, second_number):
    return first_number + second_number