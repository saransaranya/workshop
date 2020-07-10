# workshop
 > Workshop registration app
 
**Requirement**
- python 3.6

## Example
```python
workshop = Workshop('10-07-2020', 'python GIL', 2, 5)
instructor = Instructor('AAA', 'I have knowledge on GIL', skills=['python'])
attendee = Attendee('CCC', 'I want to know about GIL')
workshop.add_participant(instructor)
workshop.add_participant(attendee)
workshop.print_details()
```

- run the __init__.py file to print samples
