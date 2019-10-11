# Space Contractor!
# I-Planetary

## Motivation
This project is for the purpose of creating a website for the Space Explorer in us!

Buy futuristic Space Tech items!


## Live Site
[Live Site] (https://space-contractor-ak.herokuapp.com)

## Built With
* Flask
* MongoDB
* Jinja 2
* Python
* Heroku

## Code Example
```
# ADD items to cart
@app.route('/cart/add')
def devices_new():
    '''Create devices'''
    return render_template('cart_add.html')

# Route for POSTING SINGLE items to cart
@app.route('/cart/item', methods=['POST'])
def cart_item_post():
    '''Submit single item to cart'''
    cart= {
        'title': request.form.get('title'),
        'description': request.form.get('description')
    }
    cart_id =cart_items.insert_one(cart).inserted_id
    return redirect(url_for('item_display', cart_id=cart_id)) 

```

## Installation
1. Clone repo to local device
` git clone https://github.com/RobotGyal/Space-Contractor`
2. Install dependencies (see requirements.txt)
3. In command line run
`flask run'

## How to Use
Visit the Live Site! Test out Functionality and Enjoy!

## Contribute
Please leave feedback, bugs, etc. to this project by leaving comments and issues!

## Credits
[Contractor Project](https://docs.google.com/document/d/1C8eOyLBeGMKJ2y50QwLU5tWjNb2JVcpAE4khUBIfm0U/edit)