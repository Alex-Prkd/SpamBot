import app
import db
from schedule_post.create_schedule import ScheduleMinute


sending_post = ScheduleMinute(10, app.app, db.session_maker)
sending_post.start()
