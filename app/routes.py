from flask import Blueprint, render_template, request, redirect, url_for, session
import locale
from .helpers import obtener_user, obtener_egreso, obtener_ingreso, obtener_compra
from . import bcrypt 
from .models import Usuario, Ingreso, Egreso, Compra, Vista_total_egresos, Vista_total_ingresos
from app import db

locale.setlocale(locale.LC_ALL,'')
usuario_bp = Blueprint('usuario',__name__)
ingresos_bp = Blueprint('ingresos', __name__)
egresos_bp = Blueprint('egresos', __name__)
compras_bp = Blueprint('compras', __name__)

@usuario_bp.route('/')
def index():
    return render_template('0_welcome.html')

@usuario_bp.route('/login', methods=['GET','POST'])
def login():
    if request.method=="POST":
        user = request.form['user']
        password = request.form['password']
        exist_user =  Usuario.query.filter(Usuario.user_Id == user).first()
        if exist_user:
            if bcrypt.check_password_hash(exist_user.user_Password,password):
                mensaje="Inicio de sesión éxitoso"
                estado= True
                session['user_Id']= exist_user.user_Id
                user_id= session['user_Id']
            else:
                mensaje="Contraseña Incorrecta"
                estado= False
        else:
            mensaje="No existe un usuario con ese nombre"
            estado= False
        return render_template('1_login.html',mensaje=mensaje, estado=estado, user=user_id)
    else:
        return render_template('1_login.html')

@usuario_bp.route('/cerrar-sesion', methods=['GET', 'POST'])
def logout():
    if 'user_Id' in session:
        session.pop('user_Id', None)
        return render_template('4_cerrar_sesion.html')
    else:
        mensaje="Debes iniciar sesión primero"
        estado=False
        return render_template('1_login.html', mensaje=mensaje, estado=estado)


@usuario_bp.route('/registrarse', methods=['GET','POST'])
def registrarse():
    if request.method=="POST":
        new_user = request.form['new-user']

        new_password = bcrypt.generate_password_hash(request.form['new-password']).decode('utf-8')
        
        image= request.files['profile-image']
        image_data= image.read()
        existing_user =  Usuario.query.filter(Usuario.user_Id == new_user).first()
        if existing_user:
            mensaje="El usuario ya existe"
            return render_template('2_registro.html', mensaje=mensaje)
        else:
            new_User = Usuario(
                user_Id = new_user,
                user_Password = new_password,
                user_Img = image_data
            )
            db.session.add(new_User)
            db.session.commit()

            return render_template('1_login.html')
    else:
        return render_template('2_registro.html')
    

@usuario_bp.route('/home',methods=['GET','POST'])
def home():
    if 'user_Id' in session:
        user_id= session['user_Id']
        info_user= obtener_user(user_id)
        datos = obtener_egreso(user_id)
        datosDos= obtener_ingreso(user_id)
        datosTres= obtener_compra(user_id)
        total_egresos = db.session.query(Vista_total_egresos).first().total_egresos
        #"{:,}".format(int(db.session.query(Vista_total_egresos).first().total_egresos))
        total_ingresos = db.session.query(Vista_total_ingresos).first().total_ingresos
        #"{:,}".format(int(db.session.query(Vista_total_ingresos).first().total_ingresos))
        presupuesto = "{:,}".format(int(total_ingresos-total_egresos))

        # Verificar si hay datos disponibles, si no, enviar listas vacías
        if not datos:
            datos = []
        if not datosDos:
            datosDos = []
        if not datosTres:
            datosTres = []
        if not total_egresos:
            total_egresos="----"
        if not total_ingresos:
            total_ingresos="----"
        if not total_ingresos:
            presupuesto="----"

        return render_template('3_home.html',user=info_user, egresos=datos, ingresos=datosDos, compras=datosTres,  total_egresos=total_egresos, total_ingresos=total_ingresos, presupuesto=presupuesto)
    else:
        estado=False
        mensaje="Primero debes iniciar sesión"
        return render_template('1_login.html',estado=estado, mensaje=mensaje)
    
@usuario_bp.route('/home/<user>',methods=['GET','POST'])
def homeDos(user):
        info_user= obtener_user(user)
        return render_template('3_home.html',user=info_user)


@usuario_bp.route('/ingresos',methods=['GET','POST'])
def ingresos():
    if 'user_Id' in session:
        user_id= session['user_Id']
        if request.method=="POST":
            id= request.form['ingreso_Id']
            detalle=request.form['ingreso_Detalle']
            tipo= request.form.get('ingreso_Tipo')
            cantidad= request.form['ingreso_Cantidad']
            precio= request.form['ingreso_Precio']
            fecha= request.form['ingreso_Fecha']

            exist_ingreso =  Ingreso.query.filter(Ingreso.ingreso_Id == int(id)).first()

            if exist_ingreso:
                form="ingresos"
                return render_template('3_home.html', form=form)
            else:
                new_Ingreso= Ingreso(
                    ingreso_Id = int(id),
                    ingreso_Tipo= tipo,
                    ingreso_Detalle= detalle,
                    ingreso_Cantidad= cantidad,
                    ingreso_Precio= precio,
                    ingreso_Fecha= fecha,
                    usuario_user_Id= user_id
                )
                db.session.add(new_Ingreso)
                db.session.commit()
                return redirect(url_for('usuario.home', user=user_id))
        else:
            info_user= obtener_user(user_id)
            form="ingresos"
            return render_template('3_home.html',user=info_user, form=form)
    else:
        estado=False
        mensaje="Primero debes iniciar sesión"
        return render_template('1_login.html',estado=estado, mensaje=mensaje)

@usuario_bp.route('/egresos',methods=['GET','POST'])
def egresos():
    if 'user_Id' in session:
        user_id= session['user_Id']
        if request.method=="POST":
            
            id= request.form['egreso_Id']
            tipo= request.form.get('egreso_Tipo')
            cantidad= request.form['egreso_Cantidad']
            detalle=request.form['egreso_Detalle']
            precio= request.form['egreso_Precio']
            fecha= request.form['egreso_Fecha']
            exist_egreso =  Egreso.query.filter(Egreso.egreso_Id == int(id)).first()

            if exist_egreso:
                form="egresos"
                return render_template('3_home.html', form=form)
            else:
                new_Egreso= Egreso(
                    egreso_Id = int(id),
                    egreso_Tipo= tipo,
                    egreso_Cantidad= cantidad,
                    egreso_Precio= precio,
                    egreso_Fecha= fecha,
                    usuario_user_Id= user_id,
                    egreso_Detalle=detalle
                )
                db.session.add(new_Egreso)
                db.session.commit()
                return redirect(url_for('usuario.home', user=user_id))
        else:
            info_user= obtener_user(user_id)
            form="egresos"
            return render_template('3_home.html',user=info_user, form=form)
    else:
        estado=False
        mensaje="Primero debes iniciar sesión"
        return render_template('1_login.html',estado=estado, mensaje=mensaje)
    
@usuario_bp.route('/compras',methods=['GET','POST'])
def compras():
    if 'user_Id' in session:
        user_id= session['user_Id']
        if request.method=="POST":
            id= request.form['compra_Id']
            tipo= request.form.get('compra_Tipo')
            cantidad= request.form['compra_Cantidad']
            detalle=request.form['compra_Detalle']
            precio= request.form['compra_Precio']
            fecha= request.form['compra_Fecha']
            exist_compra =  Compra.query.filter(Compra.compra_Id == int(id)).first()

            if exist_compra:
                form="compras"
                return render_template('3_home.html', form=form)
            else:
                new_Compra= Compra(
                    compra_Id = int(id),
                    compra_Tipo= tipo,
                    compra_Cantidad= cantidad,
                    compra_Precio= precio,
                    compra_Fecha= fecha,
                    usuario_user_Id= user_id,
                    compra_Detalle= detalle
                )
                db.session.add(new_Compra)
                db.session.commit()
                return redirect(url_for('usuario.home', user=user_id))
        else:
            info_user= obtener_user(user_id)
            form="compras"
            return render_template('3_home.html',user=info_user, form=form)
    else:
        estado=False
        mensaje="Primero debes iniciar sesión"
        return render_template('1_login.html',estado=estado, mensaje=mensaje)