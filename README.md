# yuhuu...
consegui um erro maluco!


# como replicar?!
só mandar um simples `pytest` (com o `task test` o erro é diferente pq ele falha no teste anterior)

### algumas coisas interessantes
- o erro estranho acontece na linha 40 do tests/test_app.py
- só acontece qnd é executado o teste test_post_user_returns_no_password antes (se trocar os testes de posição, o erro acontece no segundo)
- se for comentada a linha 26 do conftest.py, o erro não acontece


# erro completo:
```
INTERNALERROR> Traceback (most recent call last):
INTERNALERROR>   File "/home/edinho/groups/randomlearn/fastapidozero/.venv/lib/python3.11/site-packages/_pytest/main.py", line 271, in wrap_session
INTERNALERROR>     session.exitstatus = doit(config, session) or 0
INTERNALERROR>                          ^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "/home/edinho/groups/randomlearn/fastapidozero/.venv/lib/python3.11/site-packages/_pytest/main.py", line 325, in _main
INTERNALERROR>     config.hook.pytest_runtestloop(session=session)
INTERNALERROR>   File "/home/edinho/groups/randomlearn/fastapidozero/.venv/lib/python3.11/site-packages/pluggy/_hooks.py", line 493, in __call__
INTERNALERROR>     return self._hookexec(self.name, self._hookimpls, kwargs, firstresult)
INTERNALERROR>            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "/home/edinho/groups/randomlearn/fastapidozero/.venv/lib/python3.11/site-packages/pluggy/_manager.py", line 115, in _hookexec
INTERNALERROR>     return self._inner_hookexec(hook_name, methods, kwargs, firstresult)
INTERNALERROR>            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "/home/edinho/groups/randomlearn/fastapidozero/.venv/lib/python3.11/site-packages/pluggy/_callers.py", line 152, in _multicall
INTERNALERROR>     return outcome.get_result()
INTERNALERROR>            ^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "/home/edinho/groups/randomlearn/fastapidozero/.venv/lib/python3.11/site-packages/pluggy/_result.py", line 114, in get_result
INTERNALERROR>     raise exc.with_traceback(exc.__traceback__)
INTERNALERROR>   File "/home/edinho/groups/randomlearn/fastapidozero/.venv/lib/python3.11/site-packages/pluggy/_callers.py", line 77, in _multicall
INTERNALERROR>     res = hook_impl.function(*args)
INTERNALERROR>           ^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "/home/edinho/groups/randomlearn/fastapidozero/.venv/lib/python3.11/site-packages/_pytest/main.py", line 350, in pytest_runtestloop
INTERNALERROR>     item.config.hook.pytest_runtest_protocol(item=item, nextitem=nextitem)
INTERNALERROR>   File "/home/edinho/groups/randomlearn/fastapidozero/.venv/lib/python3.11/site-packages/pluggy/_hooks.py", line 493, in __call__
INTERNALERROR>     return self._hookexec(self.name, self._hookimpls, kwargs, firstresult)
INTERNALERROR>            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "/home/edinho/groups/randomlearn/fastapidozero/.venv/lib/python3.11/site-packages/pluggy/_manager.py", line 115, in _hookexec
INTERNALERROR>     return self._inner_hookexec(hook_name, methods, kwargs, firstresult)
INTERNALERROR>            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "/home/edinho/groups/randomlearn/fastapidozero/.venv/lib/python3.11/site-packages/pluggy/_callers.py", line 152, in _multicall
INTERNALERROR>     return outcome.get_result()
INTERNALERROR>            ^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "/home/edinho/groups/randomlearn/fastapidozero/.venv/lib/python3.11/site-packages/pluggy/_result.py", line 114, in get_result
INTERNALERROR>     raise exc.with_traceback(exc.__traceback__)
INTERNALERROR>   File "/home/edinho/groups/randomlearn/fastapidozero/.venv/lib/python3.11/site-packages/pluggy/_callers.py", line 77, in _multicall
INTERNALERROR>     res = hook_impl.function(*args)
INTERNALERROR>           ^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "/home/edinho/groups/randomlearn/fastapidozero/.venv/lib/python3.11/site-packages/_pytest/runner.py", line 114, in pytest_runtest_protocol
INTERNALERROR>     runtestprotocol(item, nextitem=nextitem)
INTERNALERROR>   File "/home/edinho/groups/randomlearn/fastapidozero/.venv/lib/python3.11/site-packages/_pytest/runner.py", line 133, in runtestprotocol
INTERNALERROR>     reports.append(call_and_report(item, "call", log))
INTERNALERROR>                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "/home/edinho/groups/randomlearn/fastapidozero/.venv/lib/python3.11/site-packages/_pytest/runner.py", line 224, in call_and_report
INTERNALERROR>     report: TestReport = hook.pytest_runtest_makereport(item=item, call=call)
INTERNALERROR>                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "/home/edinho/groups/randomlearn/fastapidozero/.venv/lib/python3.11/site-packages/pluggy/_hooks.py", line 493, in __call__
INTERNALERROR>     return self._hookexec(self.name, self._hookimpls, kwargs, firstresult)
INTERNALERROR>            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "/home/edinho/groups/randomlearn/fastapidozero/.venv/lib/python3.11/site-packages/pluggy/_manager.py", line 115, in _hookexec
INTERNALERROR>     return self._inner_hookexec(hook_name, methods, kwargs, firstresult)
INTERNALERROR>            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "/home/edinho/groups/randomlearn/fastapidozero/.venv/lib/python3.11/site-packages/pluggy/_callers.py", line 130, in _multicall
INTERNALERROR>     teardown[0].send(outcome)
INTERNALERROR>   File "/home/edinho/groups/randomlearn/fastapidozero/.venv/lib/python3.11/site-packages/_pytest/skipping.py", line 266, in pytest_runtest_makereport
INTERNALERROR>     rep = outcome.get_result()
INTERNALERROR>           ^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "/home/edinho/groups/randomlearn/fastapidozero/.venv/lib/python3.11/site-packages/pluggy/_result.py", line 114, in get_result
INTERNALERROR>     raise exc.with_traceback(exc.__traceback__)
INTERNALERROR>   File "/home/edinho/groups/randomlearn/fastapidozero/.venv/lib/python3.11/site-packages/pluggy/_callers.py", line 77, in _multicall
INTERNALERROR>     res = hook_impl.function(*args)
INTERNALERROR>           ^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "/home/edinho/groups/randomlearn/fastapidozero/.venv/lib/python3.11/site-packages/_pytest/runner.py", line 368, in pytest_runtest_makereport
INTERNALERROR>     return TestReport.from_item_and_call(item, call)
INTERNALERROR>            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "/home/edinho/groups/randomlearn/fastapidozero/.venv/lib/python3.11/site-packages/_pytest/reports.py", line 362, in from_item_and_call
INTERNALERROR>     longrepr = item.repr_failure(excinfo)
INTERNALERROR>                ^^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "/home/edinho/groups/randomlearn/fastapidozero/.venv/lib/python3.11/site-packages/_pytest/python.py", line 1833, in repr_failure
INTERNALERROR>     return self._repr_failure_py(excinfo, style=style)
INTERNALERROR>            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "/home/edinho/groups/randomlearn/fastapidozero/.venv/lib/python3.11/site-packages/_pytest/nodes.py", line 486, in _repr_failure_py
INTERNALERROR>     return excinfo.getrepr(
INTERNALERROR>            ^^^^^^^^^^^^^^^^
INTERNALERROR>   File "/home/edinho/groups/randomlearn/fastapidozero/.venv/lib/python3.11/site-packages/_pytest/_code/code.py", line 701, in getrepr
INTERNALERROR>     return fmt.repr_excinfo(self)
INTERNALERROR>            ^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "/home/edinho/groups/randomlearn/fastapidozero/.venv/lib/python3.11/site-packages/_pytest/_code/code.py", line 989, in repr_excinfo
INTERNALERROR>     reprtraceback = self.repr_traceback(excinfo_)
INTERNALERROR>                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "/home/edinho/groups/randomlearn/fastapidozero/.venv/lib/python3.11/site-packages/_pytest/_code/code.py", line 913, in repr_traceback
INTERNALERROR>     entries = [
INTERNALERROR>               ^
INTERNALERROR>   File "/home/edinho/groups/randomlearn/fastapidozero/.venv/lib/python3.11/site-packages/_pytest/_code/code.py", line 914, in <listcomp>
INTERNALERROR>     self.repr_traceback_entry(entry, excinfo if last == entry else None)
INTERNALERROR>   File "/home/edinho/groups/randomlearn/fastapidozero/.venv/lib/python3.11/site-packages/_pytest/_code/code.py", line 852, in repr_traceback_entry
INTERNALERROR>     source = self._getentrysource(entry)
INTERNALERROR>              ^^^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "/home/edinho/groups/randomlearn/fastapidozero/.venv/lib/python3.11/site-packages/_pytest/_code/code.py", line 754, in _getentrysource
INTERNALERROR>     source = entry.getsource(self.astcache)
INTERNALERROR>              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "/home/edinho/groups/randomlearn/fastapidozero/.venv/lib/python3.11/site-packages/_pytest/_code/code.py", line 262, in getsource
INTERNALERROR>     astnode, _, end = getstatementrange_ast(
INTERNALERROR>                       ^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "/home/edinho/groups/randomlearn/fastapidozero/.venv/lib/python3.11/site-packages/_pytest/_code/source.py", line 185, in getstatementrange_ast
INTERNALERROR>     astnode = ast.parse(content, "source", "exec")
INTERNALERROR>               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "/usr/lib/python3.11/ast.py", line 50, in parse
INTERNALERROR>     return compile(source, filename, mode, flags,
INTERNALERROR>            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR> SystemError: AST constructor recursion depth mismatch (before=117, after=179)
```


# versoes das bibliotecas:
```
$ pip freeze
alembic==1.12.1
annotated-types==0.6.0
anyio==3.7.1
black==22.1.0
blue==0.9.1
build==1.0.3
CacheControl==0.13.1
certifi==2023.11.17
cffi==1.16.0
charset-normalizer==3.3.2
cleo==2.1.0
click==8.1.7
colorama==0.4.6
coverage==7.3.2
crashtest==0.4.1
cryptography==41.0.7
distlib==0.3.7
dnspython==2.4.2
dulwich==0.21.6
email-validator==2.1.0.post1
fastapi==0.104.1
fastjsonschema==2.19.0
filelock==3.13.1
flake8==4.0.1
greenlet==3.0.1
h11==0.14.0
httpcore==1.0.2
httpx==0.25.2
idna==3.6
importlib-metadata==6.8.0
iniconfig==2.0.0
installer==0.7.0
isort==5.12.0
jaraco.classes==3.3.0
jeepney==0.8.0
keyring==24.3.0
Mako==1.3.0
MarkupSafe==2.1.3
mccabe==0.6.1
more-itertools==10.1.0
msgpack==1.0.7
mypy-extensions==1.0.0
packaging==23.2
pathspec==0.11.2
pexpect==4.9.0
pkginfo==1.9.6
platformdirs==4.0.0
pluggy==1.3.0
poetry==1.7.1
poetry-core==1.8.1
poetry-plugin-export==1.6.0
psutil==5.9.6
ptyprocess==0.7.0
pycodestyle==2.8.0
pycparser==2.21
pydantic==2.5.2
pydantic-settings==2.1.0
pydantic_core==2.14.5
pyflakes==2.4.0
pyproject_hooks==1.0.0
pytest==7.4.3
pytest-cov==4.1.0
python-dotenv==1.0.0
rapidfuzz==3.5.2
requests==2.31.0
requests-toolbelt==1.0.0
ruff==0.1.6
SecretStorage==3.3.3
shellingham==1.5.4
sniffio==1.3.0
SQLAlchemy==2.0.23
starlette==0.27.0
taskipy==1.12.2
tomli==2.0.1
tomlkit==0.12.3
trove-classifiers==2023.11.22
typing_extensions==4.8.0
urllib3==2.1.0
uvicorn==0.24.0.post1
virtualenv==20.24.7
zipp==3.17.0
```
