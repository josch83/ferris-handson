# Form Generator

It is used for generating form from json definition.

### Usage Example

```python
from flask import render_template, url_for
from ferrisapp.app.helpers.form_generator import FormGenerator


def render_form(json_definition):
    
    return render_template(
        'ferris/generated_form.html',
        form=FormGenerator.generate(json_definition),
        form_action=url_for('SomeView.some_post_action', check_id=pk),
        confirm_btn_title="Run",
        confirm_btn_icon="play"
    )
```

### Json definition structure:

```json
{
  "fields": [
    {
      "type": "<FIELD TYPE>",
      "label": "<FIELD LABEL>",
      "name": "<FIELD NAME>",
      "required": true or false,
      "description": "<FIELD DESCRIPTION>",
      ... other field specific attributes ...
    }
  ]
}
```

Each object in `fields` represents one form field that will be rendered. All form fields are described with common attributes and those specific for certain type.

### Common Attributes

| Attr. Name | Description | Mandatory |
|------------|-------------|-----------|
|type| One of supported field types `text`, `textarea`, `file`, `int`, `float`, `select`, `multiselect`, `radio`| True
|label| Label of the field that will be rendered in the form| True
|name| Name of the field that will be sent on form submit| True
|required| Whether this field is required or not| False
|description| Description of the field. Rendered below field.| False
|default| Default value of the field | False|
|placeholder| Placeholder for the field | False|
|data| json object of key/value pairs that will be rendered as `data-key=value` attributes of the field| False| 
<br>

#### Example

```json
{
  "fields": [
    {
      "type": "text",
      "label": "First Name",
      "name": "first_name",
      "required": true,
      "description": "Insert your first name",
      "default": "John Doe",
      "placeholder": "First Name",
      "data": {
        "tooltip": "tooltip",
        "somekey": "someval"
      }
    }
  ]
}
```

will render:

```html
<input type="text" 
       name="first_name" 
       required="required" 
       value="John Doe" 
       placeholder="First Name" 
       data-tooltip="tooltip" 
       data-somekey="someval"
>
```

## Field Types

### Text 

Rendering `<input type="text">` field.

#### Additional Attributes

Described with common attributes only (no additional attributes)

#### Example 

```json
{
  "type": "text",
  "label": "Some Text",
  "name": "some_text",
  "required": true,
  "placeholder": "Type something",
  "description": "This field is required"
}
```
<br>
<br>

### Textarea

Rendering `<textarea>` field.

#### Additional Attributes

Described with common attributes only (no additional attributes)

#### Example 

```json
{
  "type": "textarea",
  "label": "Some Textarea",
  "name": "some_textarea"
}
```
<br>

### File

Rendering `<input type="file">` field. By default file will be submitted with the form. 

#### Additional Attributes

If additional `data` attributes are added to `file` field it will change it behaviour so it will perform asynchronous upload of file and only submit path to the file on storage. 

For example, if file is defined like below. when user choose file in the form that file will be uploaded to `testbucket` on Minio and only it's path will be submited with form data. 

```json
{
  "type": "file",
  "label": "Some File",
  "name": "some_file",
  "data": {
    "bucket": "testbucket",
    "async": true
  }
}
```
<br>

### Int

Rendering `<input type="number">` field.

#### Additional Attributes

| Attr. Name | Description | Mandatory |
|------------|-------------|-----------|
|step| Step of increment for number field| False
|min| Minimum value that can be submitted| False
|max| Maximum value that can be submitted| False

#### Example
```json
{
  "type": "int",
  "label": "Some Number",
  "name": "some_number",
  "default": 1,
  "min": 0,
  "max": 10,
  "step": 3
}
```
<br>
<br>

### Float

Rendering `<input type="float">` field.

#### Additional Attributes

| Attr. Name | Description | Mandatory |
|------------|-------------|-----------|
|step| Step of increment for number field| False
|min| Minimum value that can be submitted| False
|max| Maximum value that can be submitted| False

#### Example

```json
{
  "type": "float",
  "label": "Some Float",
  "name": "some_float",
  "placeholder": "0.01",
  "step": 0.03,
  "min": 0,
  "max": 10
}
```
<br>

### Select

Rendering `<select>` field.

#### Additional Attributes

| Attr. Name | Description | Mandatory |
|------------|-------------|-----------|
|choices| List of options represented as json object| True

#### Example
```json
{
  "type": "select",
  "label": "Some Select",
  "name": "some_select",
  "default": "value 2",
  "choices": [
    {
      "title": "Choice 1",
      "value": "value 1"
    },
    {
      "title": "Choice 2",
      "value": "value 2"
    },
    {
      "title": "Choice 3",
      "value": "value 3"
    }
  ]
}
```
<br>

### Multiselect

Rendering `<select multiple="multiple">` field.

#### Additional Attributes

| Attr. Name | Description | Mandatory |
|------------|-------------|-----------|
|choices| List of options represented as json object| True
|default| List of preselected values| False

#### Example

```json
{
  "type": "multiselect",
  "label": "Some MultiSelect",
  "name": "some_multiselect",
  "default": [
    "value 2",
    "value 3"
  ],
  "choices": [
    {
      "title": "Choice 1",
      "value": "value 1"
    },
    {
      "title": "Choice 2",
      "value": "value 2"
    },
    {
      "title": "Choice 3",
      "value": "value 3"
    }
  ]
}
```
<br>
<br>

### Radio

Rendering `<input type="radio">` fields.

#### Additional Attributes

| Attr. Name | Description | Mandatory |
|------------|-------------|-----------|
|choices| List of options represented as json object| True

#### Example

```json
{
  "type": "radio",
  "label": "Some Radio",
  "name": "some_radio",
  "choices": [
    {
      "title": "Choice 1",
      "value": "value 1"
    },
    {
      "title": "Choice 2",
      "value": "value 2"
    },
    {
      "title": "Choice 3",
      "value": "value 3"
    }
  ]
}
```
<br>

### Example json with all field types

```json
{
  "fields": [
    {
      "type": "text",
      "label": "Some Text",
      "name": "some_text",
      "required": true,
      "description": "This field is required"
    },
    {
      "type": "textarea",
      "label": "Some Textarea",
      "name": "some_textarea"
    },
    {
      "type": "file",
      "label": "Some File",
      "name": "some_file",
      "data": {
        "bucket": "testbucket",
        "async": true
      }
    },
    {
      "type": "int",
      "label": "Some Number",
      "name": "some_number",
      "default": 1,
      "min": 0,
      "max": 10
    },
    {
      "type": "float",
      "label": "Some Float",
      "name": "some_float",
      "placeholder": "0.01",
      "step": 0.01,
      "min": 0,
      "max": 10
    },
    {
      "type": "select",
      "label": "Some Select",
      "name": "some_select",
      "default": "value 2",
      "choices": [
        {
          "title": "Choice 1",
          "value": "value 1"
        },
        {
          "title": "Choice 2",
          "value": "value 2"
        },
        {
          "title": "Choice 3",
          "value": "value 3"
        }
      ]
    },
    {
      "type": "multiselect",
      "label": "Some MultiSelect",
      "name": "some_multiselect",
      "default": ["value 2", "value 3"],
      "choices": [
        {
          "title": "Choice 1",
          "value": "value 1"
        },
        {
          "title": "Choice 2",
          "value": "value 2"
        },
        {
          "title": "Choice 3",
          "value": "value 3"
        }
      ]
    },
    {
      "type": "radio",
      "label": "Some Radio",
      "name": "some_radio",
      "choices": [
        {
          "title": "Choice 1",
          "value": "value 1"
        },
        {
          "title": "Choice 2",
          "value": "value 2"
        },
        {
          "title": "Choice 3",
          "value": "value 3"
        }
      ]
    }
  ]
}
```





