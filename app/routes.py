from flask import Blueprint, render_template, request, redirect, url_for, session
import locale
from . import bcrypt

locale.setLocale(locale.LC_ALL,'')
usuario_bp = Blueprint('usuario',__name__)
ingresos_bp = Blueprint('ingresos', __name__)

@usuario_bp.route('/')
def index():
    return render_template('0_welcome.html')