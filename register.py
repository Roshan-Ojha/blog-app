from flask import render_template,Blueprint

register_blueprint=Blueprint("register1",__name__)
@register_blueprint.route('/Register')
def register():
    return render_template('register.html')

