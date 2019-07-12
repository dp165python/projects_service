db = sqlalchemy.create_engine(postgres_uri())
base = declarative_base()

Session = sessionmaker(db)


# class Project(base):
#     tablename = 'project'
#
#     id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
#     name = Column(String())
#     level = Column(Integer())
#     y_count = Column(Integer())
#     x_count = Column(Integer())

# if name == 'main':
    # run to create tables on server
    base.metadata.create_all(db)

    # run to drop all tables
    base.metadata.drop_all(db)