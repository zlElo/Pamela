<h1>Pamela</h1>
<hr><p>Pamela is a python library to simplify API usage in programs</p><h2>General Information</h2>
<hr><ul>
<li>Pamela is a python library to simplify API usage in programs. It has different features to optimize the workflow with APIs.</li>
</ul><ul>
<li>API usage in programs is sometimes very annoying. To optimize all things connected with APIs, Pamela is your helper!</li>
</ul><h2>Technologies Used</h2>
<hr><ul>
<li>Python</li>
</ul><ul>
<li>Requests</li>
</ul><h2>Features</h2>
<hr><ul>
<li>Receive data</li>
</ul><ul>
<li>Create sessions</li>
</ul><ul>
<li>Get status of session</li>
</ul><ul>
<li>Choose file format</li>
</ul><ul>
<li>Save response to json</li>
</ul><h2>Setup</h2>
<hr><p>You can install Pamela in two ways: via PyPi or the setup.py file.</p><h5>Steps</h5><ul>
<li>pip install pamela</li>
</ul><h2>Code examples (simple)</h2>
```py
# import pamela with all classes
from pamela import Pamela, Session

# create pamela instance
pamela = Pamela()

# create session with pamela
session1 = Session.create("address", "username", "password")

# status of session
status_session = Session.status(address="address", session=session1)

# receive data with session
answer = pamela.receive_data(address="address", session=session1)

# receive data with no credentials
answer = pamela.receive_data(address="address")
```

</ul><h2>Contact</h2>
<hr><p><span style="margin-right: 30px;"></span><a href="https://github.com/zlElo"><img target="_blank" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" style="width: 10%;"></a></p>
