from flask import Blueprint, url_for, request, render_template, g
from pybo.models import Question, Answer
from pybo.forms import AnswerForm
from datetime import datetime
from pybo import db
from werkzeug.utils import redirect
from pybo.views.user_views import login_required

bp = Blueprint('answer', __name__, url_prefix='/answer')

@bp.route('/create/<int:question_id>', methods=('POST',))
@login_required
# def create(question_id):
#     question = Question.query.get_or_404(question_id)
#     content = request.form['content']
#     answer = Answer(content=content, create_date=datetime.now())
#     question.answer_set.append(answer)
#     db.session.commit()
#     return redirect(url_for('question.detail', question_id=question_id))
def create(question_id):
    form=AnswerForm()
    question = Question.query.get_or_404(question_id)

    if form.validate_on_submit():    
        content = request.form['content']
        answer = Answer(content=content, create_date=datetime.now(), user=g.user)
        question.answer_set.append(answer)
        db.session.commit()
        return redirect(url_for('question.detail', question_id=question_id))
    return render_template('question/question_detail.html', form=form, question=question)