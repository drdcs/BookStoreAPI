from fastapi import APIRouter
from app.api.routes.books import router as books_router
from app.api.routes.authors import router as author_router


router = APIRouter()

router.include_router(books_router, prefix="/books", tags=["books"])
router.include_router(author_router, prefix="/authors", tags=["authors"])