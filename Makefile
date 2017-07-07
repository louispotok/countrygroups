all: data/unfccc.csv data/annex-one.csv data/non-annex-one.csv data/ldcs.csv data/graduated-ldcs.csv data/eu-member-states.csv data/sids.csv data/sids-non-un-or-regional-commissions-associates.csv data/g20.csv

data/unfccc.csv: scripts/unfccc.py venv
	@echo $@
	@./venv/bin/python $<

data/annex-one.csv: scripts/annex-one.py venv
	@echo $@
	@./venv/bin/python $<

data/non-annex-one.csv: scripts/non-annex-one.py venv
	@echo $@
	@./venv/bin/python $<

data/ldcs.csv data/graduated-ldcs.csv: scripts/ldcs.py
	@echo $@
	@./venv/bin/python $<

data/eu-member-states.csv: scripts/eu-member-states.py
	@echo $@
	@./venv/bin/python $<

data/sids.csv data/sids-non-un-or-regional-commissions-associates.csv: scripts/sids.py
	@echo $@
	@./venv/bin/python $<

data/g20.csv: scripts/g20.py
	@echo $@
	@./venv/bin/python $<

venv: scripts/requirements.txt
	[ -d ./venv ] || python3 -m venv venv
	./venv/bin/pip install --upgrade pip
	./venv/bin/pip install -Ur $<
	touch venv

clean:
	rm -rf data/*.csv venv

.PHONY: clean
