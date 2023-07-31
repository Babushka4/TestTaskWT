from sqlalchemy import Table, Column, MetaData, Integer, String, Boolean, ForeignKey

metadata = MetaData()

user = Table(
    'user',
    metadata,
    Column('id', Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column('email', String(length=320), unique=True, index=True, nullable=False),
    Column('hashed_password', String(length=1024), nullable=False),
    Column('is_active', Boolean, default=True, nullable=False),
    Column('is_superuser', Boolean, default=False, nullable=False),
    Column('is_verified', Boolean, default=False, nullable=False)
)

post = Table(
    'post',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('text', String, nullable=False),
    Column('user_id', ForeignKey('user.id'))
)

like = Table(
    'like',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('user_liked', ForeignKey('user.id')),
    Column('post_liked', ForeignKey('post.id'))
)
