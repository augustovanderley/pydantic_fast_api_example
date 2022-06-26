#!/bin/bash

uvicorn main:app --reload > log.txt 2>&1 &