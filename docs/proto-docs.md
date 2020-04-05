# Protocol Documentation
<a name="top"></a>

## Table of Contents

- [task.proto](#task.proto)
    - [AssignTaskRequest](#task.v1.AssignTaskRequest)
    - [CreateTaskRequest](#task.v1.CreateTaskRequest)
    - [DeleteTaskRequest](#task.v1.DeleteTaskRequest)
    - [NearbyRequest](#task.v1.NearbyRequest)
    - [NearbyResult](#task.v1.NearbyResult)
    - [SetStatusRequest](#task.v1.SetStatusRequest)
    - [Tag](#task.v1.Tag)
    - [TagsRequest](#task.v1.TagsRequest)
    - [TagsResult](#task.v1.TagsResult)
    - [Task](#task.v1.Task)
    - [UUID](#task.v1.UUID)
  
    - [Status](#task.v1.Status)
  
  
    - [TaskService](#task.v1.TaskService)
  

- [user.proto](#user.proto)
    - [CreateUserRequest](#user.v1.CreateUserRequest)
    - [DeleteUserRequest](#user.v1.DeleteUserRequest)
    - [NearbyRequest](#user.v1.NearbyRequest)
    - [NearbyResult](#user.v1.NearbyResult)
    - [Review](#user.v1.Review)
    - [ReviewRequest](#user.v1.ReviewRequest)
    - [ReviewResponse](#user.v1.ReviewResponse)
    - [SubmitReviewRequest](#user.v1.SubmitReviewRequest)
    - [TagsResult](#user.v1.TagsResult)
    - [TaskResult](#user.v1.TaskResult)
    - [UUID](#user.v1.UUID)
    - [UpdateScoreRequest](#user.v1.UpdateScoreRequest)
    - [User](#user.v1.User)
    - [UserTagsRequest](#user.v1.UserTagsRequest)
    - [UserTaskRequest](#user.v1.UserTaskRequest)
  
    - [Role](#user.v1.Role)
  
  
    - [UserService](#user.v1.UserService)
  

- [Scalar Value Types](#scalar-value-types)



<a name="task.proto"></a>
<p align="right"><a href="#top">Top</a></p>

## task.proto



<a name="task.v1.AssignTaskRequest"></a>

### AssignTaskRequest
DeleteTaskRequest represents a request to to assign a task to a user


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| user_id | [UUID](#task.v1.UUID) |  |  |
| task_id | [UUID](#task.v1.UUID) |  |  |






<a name="task.v1.CreateTaskRequest"></a>

### CreateTaskRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) |  | task name |
| description | [string](#string) |  | task description langth should be limited |
| tag | [string](#string) |  | tag |
| points | [int32](#int32) |  | y/n ? |






<a name="task.v1.DeleteTaskRequest"></a>

### DeleteTaskRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| task_id | [UUID](#task.v1.UUID) |  |  |






<a name="task.v1.NearbyRequest"></a>

### NearbyRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| lat | [float](#float) |  |  |
| lon | [float](#float) |  |  |
| radius | [int32](#int32) |  |  |






<a name="task.v1.NearbyResult"></a>

### NearbyResult



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| tasks | [Task](#task.v1.Task) | repeated |  |






<a name="task.v1.SetStatusRequest"></a>

### SetStatusRequest
SetStatusRequest represents a request to set the status of a task


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| task_id | [UUID](#task.v1.UUID) |  |  |
| status | [Status](#task.v1.Status) |  | status UNASSIGEND, ASSIGNED, COMPLETED |






<a name="task.v1.Tag"></a>

### Tag



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) |  |  |
| count | [int32](#int32) |  |  |






<a name="task.v1.TagsRequest"></a>

### TagsRequest
TagsRequest represents a request to list the current tags ordered by count given a start date


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| created_since | [google.protobuf.Timestamp](#google.protobuf.Timestamp) |  |  |






<a name="task.v1.TagsResult"></a>

### TagsResult



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| tags | [Tag](#task.v1.Tag) | repeated |  |






<a name="task.v1.Task"></a>

### Task
Task represents a Task object


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [UUID](#task.v1.UUID) |  |  |
| name | [string](#string) |  |  |
| status | [Status](#task.v1.Status) |  |  |
| submission_tstamp | [google.protobuf.Timestamp](#google.protobuf.Timestamp) |  |  |
| description | [string](#string) |  |  |
| tag | [string](#string) |  |  |
| points | [int32](#int32) |  |  |
| completed_tstamp | [google.protobuf.Timestamp](#google.protobuf.Timestamp) |  |  |






<a name="task.v1.UUID"></a>

### UUID



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| value | [string](#string) |  |  |





 


<a name="task.v1.Status"></a>

### Status


| Name | Number | Description |
| ---- | ------ | ----------- |
| UNASSIGEND | 0 |  |
| ASSIGNED | 1 |  |
| COMPLETED | 2 |  |


 

 


<a name="task.v1.TaskService"></a>

### TaskService


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| Nearby | [NearbyRequest](#task.v1.NearbyRequest) | [NearbyResult](#task.v1.NearbyResult) |  |
| Create | [CreateTaskRequest](#task.v1.CreateTaskRequest) | [Task](#task.v1.Task) |  |
| Delete | [DeleteTaskRequest](#task.v1.DeleteTaskRequest) | [Task](#task.v1.Task) |  |
| Assign | [AssignTaskRequest](#task.v1.AssignTaskRequest) | [Task](#task.v1.Task) |  |
| SetStatus | [SetStatusRequest](#task.v1.SetStatusRequest) | [Task](#task.v1.Task) |  |
| ListTags | [TagsRequest](#task.v1.TagsRequest) | [TagsResult](#task.v1.TagsResult) |  |

 



<a name="user.proto"></a>
<p align="right"><a href="#top">Top</a></p>

## user.proto



<a name="user.v1.CreateUserRequest"></a>

### CreateUserRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| role | [Role](#user.v1.Role) |  | Indicates the users Role (Helper, Needer) |
| name | [string](#string) |  |  |
| phone_number | [int32](#int32) |  |  |






<a name="user.v1.DeleteUserRequest"></a>

### DeleteUserRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| user_id | [UUID](#user.v1.UUID) |  |  |






<a name="user.v1.NearbyRequest"></a>

### NearbyRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| lat | [float](#float) |  |  |
| lon | [float](#float) |  |  |
| radius | [int32](#int32) |  |  |
| role | [Role](#user.v1.Role) |  |  |






<a name="user.v1.NearbyResult"></a>

### NearbyResult



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| users | [User](#user.v1.User) | repeated |  |






<a name="user.v1.Review"></a>

### Review



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [UUID](#user.v1.UUID) |  |  |
| review | [string](#string) |  |  |
| rating | [int32](#int32) |  |  |
| created_tstamp | [google.protobuf.Timestamp](#google.protobuf.Timestamp) |  |  |






<a name="user.v1.ReviewRequest"></a>

### ReviewRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| user_id | [UUID](#user.v1.UUID) |  |  |






<a name="user.v1.ReviewResponse"></a>

### ReviewResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| reviews | [Review](#user.v1.Review) | repeated |  |






<a name="user.v1.SubmitReviewRequest"></a>

### SubmitReviewRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| user_id | [UUID](#user.v1.UUID) |  |  |
| review | [string](#string) |  | Review string, should probably be limited in length |
| rating | [int32](#int32) |  | User rating between 1-5 |






<a name="user.v1.TagsResult"></a>

### TagsResult



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| tags | [string](#string) | repeated | list of user tags |






<a name="user.v1.TaskResult"></a>

### TaskResult



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| tasks | [task.v1.Task](#task.v1.Task) | repeated |  |






<a name="user.v1.UUID"></a>

### UUID



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| value | [string](#string) |  |  |






<a name="user.v1.UpdateScoreRequest"></a>

### UpdateScoreRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| user_id | [UUID](#user.v1.UUID) |  |  |
| value | [int32](#int32) |  |  |






<a name="user.v1.User"></a>

### User



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [UUID](#user.v1.UUID) |  |  |
| name | [string](#string) |  |  |
| phone_number | [int32](#int32) |  |  |
| joined_tstamp | [google.protobuf.Timestamp](#google.protobuf.Timestamp) |  |  |
| role | [Role](#user.v1.Role) |  | HLPR, NDR |
| avg_rating | [float](#float) |  |  |
| score | [int32](#int32) |  |  |
| city | [string](#string) |  |  |
| country | [string](#string) |  |  |
| postalCode | [string](#string) |  |  |
| lat | [float](#float) |  |  |
| lon | [float](#float) |  |  |
| reviews | [Review](#user.v1.Review) |  |  |
| tasks | [task.v1.Task](#task.v1.Task) |  |  |






<a name="user.v1.UserTagsRequest"></a>

### UserTagsRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| user_id | [UUID](#user.v1.UUID) |  |  |






<a name="user.v1.UserTaskRequest"></a>

### UserTaskRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| user_id | [UUID](#user.v1.UUID) |  |  |
| status | [task.v1.Status](#task.v1.Status) |  |  |





 


<a name="user.v1.Role"></a>

### Role


| Name | Number | Description |
| ---- | ------ | ----------- |
| HLPR | 0 |  |
| NEEDR | 1 |  |


 

 


<a name="user.v1.UserService"></a>

### UserService


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| Create | [CreateUserRequest](#user.v1.CreateUserRequest) | [User](#user.v1.User) |  |
| Delete | [DeleteUserRequest](#user.v1.DeleteUserRequest) | [User](#user.v1.User) |  |
| Nearby | [NearbyRequest](#user.v1.NearbyRequest) | [NearbyResult](#user.v1.NearbyResult) |  |
| Reviews | [ReviewRequest](#user.v1.ReviewRequest) | [ReviewResponse](#user.v1.ReviewResponse) |  |
| SubmitReview | [SubmitReviewRequest](#user.v1.SubmitReviewRequest) | [Review](#user.v1.Review) |  |
| UpdateScore | [UpdateScoreRequest](#user.v1.UpdateScoreRequest) | [User](#user.v1.User) |  |
| UserTags | [UserTagsRequest](#user.v1.UserTagsRequest) | [TagsResult](#user.v1.TagsResult) |  |
| UserTasks | [UserTaskRequest](#user.v1.UserTaskRequest) | [TaskResult](#user.v1.TaskResult) |  |

 



## Scalar Value Types

| .proto Type | Notes | C++ | Java | Python | Go | C# | PHP | Ruby |
| ----------- | ----- | --- | ---- | ------ | -- | -- | --- | ---- |
| <a name="double" /> double |  | double | double | float | float64 | double | float | Float |
| <a name="float" /> float |  | float | float | float | float32 | float | float | Float |
| <a name="int32" /> int32 | Uses variable-length encoding. Inefficient for encoding negative numbers – if your field is likely to have negative values, use sint32 instead. | int32 | int | int | int32 | int | integer | Bignum or Fixnum (as required) |
| <a name="int64" /> int64 | Uses variable-length encoding. Inefficient for encoding negative numbers – if your field is likely to have negative values, use sint64 instead. | int64 | long | int/long | int64 | long | integer/string | Bignum |
| <a name="uint32" /> uint32 | Uses variable-length encoding. | uint32 | int | int/long | uint32 | uint | integer | Bignum or Fixnum (as required) |
| <a name="uint64" /> uint64 | Uses variable-length encoding. | uint64 | long | int/long | uint64 | ulong | integer/string | Bignum or Fixnum (as required) |
| <a name="sint32" /> sint32 | Uses variable-length encoding. Signed int value. These more efficiently encode negative numbers than regular int32s. | int32 | int | int | int32 | int | integer | Bignum or Fixnum (as required) |
| <a name="sint64" /> sint64 | Uses variable-length encoding. Signed int value. These more efficiently encode negative numbers than regular int64s. | int64 | long | int/long | int64 | long | integer/string | Bignum |
| <a name="fixed32" /> fixed32 | Always four bytes. More efficient than uint32 if values are often greater than 2^28. | uint32 | int | int | uint32 | uint | integer | Bignum or Fixnum (as required) |
| <a name="fixed64" /> fixed64 | Always eight bytes. More efficient than uint64 if values are often greater than 2^56. | uint64 | long | int/long | uint64 | ulong | integer/string | Bignum |
| <a name="sfixed32" /> sfixed32 | Always four bytes. | int32 | int | int | int32 | int | integer | Bignum or Fixnum (as required) |
| <a name="sfixed64" /> sfixed64 | Always eight bytes. | int64 | long | int/long | int64 | long | integer/string | Bignum |
| <a name="bool" /> bool |  | bool | boolean | boolean | bool | bool | boolean | TrueClass/FalseClass |
| <a name="string" /> string | A string must always contain UTF-8 encoded or 7-bit ASCII text. | string | String | str/unicode | string | string | string | String (UTF-8) |
| <a name="bytes" /> bytes | May contain any arbitrary sequence of bytes. | string | ByteString | str | []byte | ByteString | string | String (ASCII-8BIT) |

