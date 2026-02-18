## 0.7.0 (2026-02-18)

### Feat

- **ci.yml**: add continous integretion

## 0.6.0 (2026-02-17)

### Feat

- **counter.py**: add counter that will act as a decorator

### Refactor

- **src**: redo folder structure

## 0.5.1 (2026-02-17)

### Refactor

- **pyproject.toml**: remove second version variable

## 0.5.0 (2026-02-17)

### Fix

- **pyproject.toml**: manually change version to 0.4.3 in accordance to error msg
- **pyproject.toml**: correct spelling mistake that causing bumping failure
- **pyproject.toml**: fix the config for bumping versions

## 0.4.1 (2026-02-17)

### Refactor

- **src,-tests**: change folder structure to adhare to deployment standards

## 0.4.0 (2026-02-16)

### Feat

- **test_password_generator.py**: add test for string and empty inputs

## 0.3.0 (2026-02-16)

### Feat

- **password_generator.py**: add handling for float input

### Refactor

- **src,test**: change folder structure to make imports possible

## 0.2.2 (2026-02-15)

### Refactor

- **password_generator.py**: change name of function from password_generator to password_engine

## 0.2.1 (2026-02-15)

### Refactor

- **password_generator.py**: add logic to detect when password length is less than 10

## 0.2.0 (2026-02-14)

### Feat

- **main.py-&-password_generator.py**: move code into password_generator and do a refactor

### Refactor

- **password_generator.py**: add an exception to handle input less than 10
