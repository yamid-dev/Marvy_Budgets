from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

db = SQLAlchemy()
class Vista_total_ingresos(db.Model):
    __table__ = db.Table(
        'vista_total_ingresos',
        db.metadata,
        db.Column('total_ingresos', db.Float, primary_key=True)
    )
class Vista_total_egresos(db.Model):
    __table__ = db.Table(
        'vista_total_egresos',
        db.metadata,
        db.Column('total_egresos', db.Float, primary_key=True)
    )
class Usuario(db.Model):
    __tablename__ = 'usuario'
    user_Id = db.Column(db.String(65), primary_key=True)
    user_Password = db.Column(db.String(255))
    user_Img = db.Column(db.LargeBinary)
class Ingreso(db.Model):
    __tablename__ = 'ingreso'
    ingreso_Id = db.Column(db.Integer, primary_key=True)
    ingreso_Detalle= db.Column(db.String(100))
    ingreso_Tipo= db.Column(db.String(65))
    ingreso_Cantidad = db.Column(db.Integer)
    ingreso_Precio = db.Column(db.Float)
    ingreso_Fecha = db.Column(db.Date)
    ingreso_Total = db.Column(db.Float, db.Computed('(ingreso_Precio * ingreso_Cantidad)'))
    usuario_user_Id = db.Column(db.Integer, db.ForeignKey('usuario.user_Id'))

class Egreso(db.Model):
    __tablename__ = 'egreso'
    egreso_Id = db.Column(db.Integer, primary_key=True)
    egreso_Detalle= db.Column(db.String(100))
    egreso_Tipo= db.Column(db.String(65))
    egreso_Cantidad = db.Column(db.Integer)
    egreso_Precio = db.Column(db.Float)
    egreso_Fecha = db.Column(db.Date)
    egreso_Total = db.Column(db.Float, db.Computed('(egreso_Precio * egreso_Cantidad)'))
    usuario_user_Id = db.Column(db.Integer, db.ForeignKey('usuario.user_Id'))

class Compra(db.Model):
    __tablename__ = 'compra'
    compra_Id = db.Column(db.Integer, primary_key=True)
    compra_Detalle= db.Column(db.String(100))
    compra_Tipo= db.Column(db.String(65))
    compra_Cantidad = db.Column(db.Integer)
    compra_Precio = db.Column(db.Float)
    compra_Fecha = db.Column(db.Date)
    compra_Total = db.Column(db.Float, db.Computed('(compra_Precio * compra_Cantidad)'))
    compra_Check= db.Column(db.Integer)
    usuario_user_Id = db.Column(db.Integer, db.ForeignKey('usuario.user_Id'))