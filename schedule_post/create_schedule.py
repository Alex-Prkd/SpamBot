from apscheduler.schedulers.asyncio import AsyncIOScheduler

from app.handlers.event import send_post


class ScheduleMinute:
    def __init__(self, interval: int,
                 client, session):
        self.schedule = AsyncIOScheduler()
        self.schedule.add_job(send_post, trigger="interval",
                              minutes=interval,
                              args=[client, session],
                              id="1")

    def start(self):
        self.schedule.start()

    def edit_schedule_minute(self, interval: int):
        self.schedule.reschedule_job(job_id="1",
                                     trigger="interval",
                                     minutes=interval)

    def edit_schedule_hour(self, interval: int):
        self.schedule.reschedule_job(job_id="1",
                                     trigger="interval",
                                     hours=interval)

    def pause_schedule(self):
        self.schedule.pause()

    def resume_schedule(self):
        self.schedule.resume()

    def info_schedule(self):
        return self.schedule.get_job(job_id="1")

