
from fastapi import APIRouter

from app.dtos.create_meeting_response import CreateMeetingResponse

edgedb_router = APIRouter(prefix="/v1/edgedb/meeting", tags=["meeting"], redirect_slashes=False)
mysql_router = APIRouter(prefix="/v1/mysql/meeting", tags=["meeting"], redirect_slashes=False)


@edgedb_router.post(
    "",
    description="meeting 을 생성합니다.",
)
async def api_create_meeting_edgedb() -> CreateMeetingResponse:
    return CreateMeetingResponse(url_code="abc")


@mysql_router.post("", description="meeting 을 생성합니다.")
async def api_create_meeting_myql() -> CreateMeetingResponse:
    return CreateMeetingResponse(url_code="abc")
