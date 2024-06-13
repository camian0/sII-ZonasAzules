from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from helpers.dtos.responseDto import ResponseDto
from helpers.statusCodes import BAD_REQUEST

async def validation_exception_handler(request: Request, exc: RequestValidationError):
    print(exc.errors())
    print(exc.errors()[0]["type"])
    errors = exc.errors()
    error_msg = "Errores en la solicitud, por favor revise que los datos que está enviando sean correctos"
    responseDto = ResponseDto()
    responseDto.status = BAD_REQUEST
    responseDto.message = error_msg
    return JSONResponse(
        status_code=400,
        content=jsonable_encoder(responseDto.toString())
    )