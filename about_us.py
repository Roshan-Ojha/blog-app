from flask import render_template,Blueprint
about_blueprint=Blueprint('about',__name__)

@about_blueprint.route('/About')
def about():
    return render_template('About_Us.html')