class TaskGenerationError(Exception):
    """Task generation failed after retry attempts"""

    pass


class TaskValidationError(Exception):
    pass
