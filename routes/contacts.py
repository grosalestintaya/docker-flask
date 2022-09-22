from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.contact import Contact
from utils.db import db
from Forms.form1 import NamerForm

contacts = Blueprint("contacts", __name__)


@contacts.route('/')
def index():
    contacts = Contact.query.all()
    return render_template('index.html', contacts=contacts)


@contacts.route('/face')
def face():
    frist_name = 'Julio'
    stuff = 'This is bold text'
    flash("Welcome To Our Website!")
    favorite_pizza = ['peperony', 'chenesy', 'Familiar', 41]
    return render_template('face.html', frist_name=frist_name,
                           stuff=stuff,
                           favorite_pizza=favorite_pizza)



@contacts.route('/new', methods=['POST'])
def add_contact():
    if request.method == 'POST':

        # receive data from the form
        fullname = request.form['fullname']
        email = request.form['email']
        phone = request.form['phone']

        # create a new Contact object
        new_contact = Contact(fullname, email, phone)
        # save the object into the database
        db.session.add(new_contact)
        db.session.commit()

        flash('Contact added successfully!')

        return redirect(url_for('contacts.index'))


@contacts.route("/update/<string:id>", methods=["GET", "POST"])
def update(id):
    # get contact by Id
    print(id)
    contact = Contact.query.get(id)

    if request.method == "POST":
        contact.fullname = request.form['fullname']
        contact.email = request.form['email']
        contact.phone = request.form['phone']

        db.session.commit()

        flash('Contact updated successfully!')

        return redirect(url_for('contacts.index'))

    return render_template("update.html", contact=contact)


@contacts.route("/delete/<id>", methods=["GET"])
def delete(id):
    contact = Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()

    flash('Contact deleted successfully!')

    return redirect(url_for('contacts.index'))


@contacts.route("/about")
def about():
    return render_template("about.html")


@contacts.route("/new_user")
def new_user(id):
    contact = Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()

    flash('Contact deleted successfully!')

    return redirect(url_for('contacts.index'))





@contacts.route('/user/<name>')
def user(name):
    return render_template('user.html',
                           user_name=name)


@contacts.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NamerForm()
    # Validate Form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash("From Submitted Successfully!")

    return render_template('name.html',
                           name=name,
                           form=form)                    