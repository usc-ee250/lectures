#!/bin/sh
curl -L -H "Accept: application/vnd.github+json" https://api.github.com/repos/usc-ee250/lectures/activity?activity_type=push
