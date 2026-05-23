class TaskScheduler:
    def __init__(self):
        self.tasks = {}
    
    def add_task(self, task_id, func):
        self.tasks[task_id] = func
