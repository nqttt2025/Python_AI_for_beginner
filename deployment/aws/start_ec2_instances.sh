#!/bin/bash

# **Important:**  Configure AWS CLI first!  You need to have the AWS CLI installed and configured with your credentials (access key, secret key, region).  Use `aws configure` to set this up.

# Replace with your actual instance IDs
# INSTANCE_IDS=("i-04c58846101081252" "i-yyyyyyyyyyyyyyyyy" "i-zzzzzzzzzzzzzzz" "i-aaaaaaaaaaaaaaaaa" "i-bbbbbbbbbbbbbbbbb")
INSTANCE_IDS=("i-04c58846101081252")

# Function to get the status of an instance
function get_instance_status() {
    local instance_id="$1"
    local STATUS_INS=$(aws ec2 describe-instances --instance-ids "$instance_id" --query "Reservations[0].Instances[0].State.Name" --output text)
    echo "${STATUS_INS}"
}

function show_instance_status() {
    local STATUS_INS="$1"
    case "$STATUS_INS" in
        pending)
            echo "Instance $instance_id is in pending state."
            ;;
        running)
            echo "Instance $instance_id is running."
            ;;
        stopping)
            echo "Instance $instance_id is stopping."
            ;;
        stopped)
            echo "Instance $instance_id is stopped."
            ;;
        shutting-down)
            echo "Instance $instance_id is shutting down."
            ;;
        terminated)
            echo "Instance $instance_id is terminated."
            ;;
        *)
            echo "Instance $instance_id has an unknown status: $instance_status"
            ;;
    esac
}

function start_instance() {
  local instance_id="$1"
  local STATUS_INS=$(get_instance_status "$instance_id")
  show_instance_status "$STATUS_INS"
  if [ "$STATUS_INS" == "stopped" ]; then
    echo "Starting instance: $instance_id"
    aws_start_ins_log=$(aws ec2 start-instances --instance-ids "$instance_id")
    echo "$aws_start_ins_log"
    # Check if the start command was successful
    if [ $? -eq 0 ]; then
      echo "Successfully started instance: $instance_id"
    else
      echo "Failed to start instance: $instance_id"
    fi
  else
    echo "Instance $instance_id is not in a stopped state. Current status: $STATUS_INS"
  fi
}

############################################################################ Main Script ############################################################################

function main() {
    # Loop through the instance IDs and start each one
    for instance_id in "${INSTANCE_IDS[@]}"; do
        start_instance "$instance_id"
    done
    echo "Finished attempting to start instances."
}

main