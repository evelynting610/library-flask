from library.extensions import ma, db
from library.models import Request


class RequestSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Request
        sqla_session = db.session
        fields = ('book_id', 'title', 'available', 'user_id', 'requested_at')
        dump_only = ('book_id', 'title', 'available', 'user_id', 'requested_at')
