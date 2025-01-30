from functools import cached_property
from typing import List
from pydantic import Field, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    private_key_hex: str = Field(..., min_length=1)
    relays: str = Field(..., min_length=1)
    profile_display_pic_url: str = Field(..., min_length=1)
    profile_display_name: str = Field(..., min_length=1)
    profile_about: str = Field(..., min_length=1)
    redis_broker_url: str = Field(..., min_length=1)
    redis_backend_url: str = Field(..., min_length=1)
    cron_hours: int = Field(default=1)
    cron_minutes: int = Field(default=1)

    @computed_field
    @cached_property
    def relays_list(self) -> List[str]:
        return [r.strip() for r in self.relays.split(",")]
