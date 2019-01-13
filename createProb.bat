rem usage: createProb TwoSum_LC001
for /f "tokens=1,2 delims=_" %%a in ("%1") do (
  set BEFORE_UNDERSCORE=%%a
  set AFTER_UNDERSCORE=%%b
)

md %1 
cd %1
md java
md py
md question
cd java
type nul >%BEFORE_UNDERSCORE%.java
cd ..\py
type nul >%BEFORE_UNDERSCORE%.py
cd ..\question
type nul >%BEFORE_UNDERSCORE%.md
cd ..\..
