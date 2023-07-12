import config
from db.engine import added_engine, create_session

engine = added_engine(config.SettingsBot.DATABASE)
session_maker = create_session(engine)