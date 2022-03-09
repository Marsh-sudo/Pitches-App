from flask_login import login_required
from flask import render_template,request,redirect,url_for,abort
from models import Pitch, User,Upvote,D
from . import main
from .forms import PitchForm
from .forms import UpdateProfile
from .. import db,photos

@main.route('/')
def index():
    '''
    view root page function
    '''
    #categories build up
    pickuplines = Pitch.query.filter_by('pickuplines')
    motivationalpitch = Pitch.query.filter_by('motivationalpitch')

    title = 'The Pitch App'

    return render_template('index.html',title = title, pickuplines = pickuplines, motivationalpitch = motivationalpitch)
     

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html",user = user)


@main.route('/user/<uname>/update', methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form=form)

@main.route('/user/<uname>/update/pic',methods = ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/pitch/', methods = ['GET','POST'])
@login_required
def new_pitch():
    form = PitchForm()

    if form.validate_on_submit():
        description = form.description.data
        title = form.title.data
        category = form.category.data

        new_pitch = Pitch(title=title,description=description,category=category)

        db.session.add(new_pitch)
        db.session.commit()

        return redirect(url_for('main.index'))

    return render_template('pitch.htm', form=form)


@main.route('/pitch/upvote/<int:pitch_id>/upvote' , methods = ['GET','POST'])
@login_required
def upvote(pitch_id):
    pitch = Pitch.query.get(pitch_id)
    pitch_upvote = Upvote.query.filter_by(pitch_id=pitch)

    if Upvote.query.filter(Upvote.pitch_id==pitch_upvote).first():
        return redirect(url_for('main.idex'))

    new_upvote = Upvote(pitch_id=pitch_id)
    new_upvote.save_upvotes()
    return redirect(url_for('main.index'))