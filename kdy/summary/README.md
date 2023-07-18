# Summary

1. chat gpt api를 활용하여 summary를 진행할 것,
   - document: https://platform.openai.com/docs/api-reference/chat
   
## farameter
   - model: 사용할 모델의 ID
   - messages: 지금까지의 대화를 구성하는 메시지 목록
      - role: 메시지 작성자의 역할
      - content: 메시지의 내용입니다. 는 모든 메시지에 필요하며 함수 호출이 있는 도우미 메시지의 경우 null일 수 있습니다
      - name: 이 메시지를 만든 사람의 이름입니다. role이 인 경우 필수이며, 응답이 . a-z, A-Z, 0-9 및 밑줄을 포함할 수 있으며 최대 길이는 64자입니다
      - fuction_call: 모델에 의해 생성된 대로 호출해야 하는 함수의 이름과 인수
   - functions: 모델이 JSON 입력을 생성할 수 있는 함수 목록
      - name: 호출할 함수의 이름입니다. a-z, A-Z, 0-9이거나 밑줄과 대시를 포함해야 하며 최대 길이는 64입니다.
      - discription: 함수가 수행하는 작업에 대한 설명으로, 모델에서 함수를 호출하는 시기와 방법을 선택하는 데 사용됩니다.
      - parameters: 함수가 허용하는 매개 변수로, JSON 스키마 개체로 설명됩니다. 
   - function_call
    모델이 함수 호출에 응답하는 방식을 제어합니다. "none"은 모델이 함수를 호출하지 않고 최종 사용자에게 응답한다는 것을 의미합니다. "자동"은 모델이 최종 사용자 또는 함수 호출 중에서 선택할 수 있음을 의미합니다. 를 통해 특정 함수를 지정하면 모델이 해당 함수를 호출하게 됩니다. "none"은 함수가 없을 때의 기본값입니다. "auto"는 함수가 있는 경우 기본값입니다.{"name":\ "my_function"}
   - temperature
   0에서 2 사이의 사용할 샘플링 온도. 0.8과 같은 값이 높을수록 출력이 더 무작위화되고 0.2와 같은 값이 낮을수록 더 집중적이고 결정적입니다.

   일반적으로 이 방법을 변경하거나 둘 다 변경하지 않는 것이 좋습니다.top_p
   - top_p
   핵 샘플링이라고 하는 온도로 샘플링하는 대안으로, 모델은 확률 질량top_p 가진 토큰의 결과를 고려합니다. 따라서 0.1은 상위 10% 확률 질량을 구성하는 토큰만 고려됨을 의미합니다.

   일반적으로 이 방법을 변경하거나 둘 다 변경하지 않는 것이 좋습니다.temperature
   - n: 각 입력 메시지에 대해 생성할 채팅 완료 선택 항목 수입니다.
   - stream: 설정하면 ChatGPT에서와 같이 부분 메시지 델타가 전송됩니다. 토큰은 사용 가능해지면 데이터 전용 서버 전송 이벤트로 전송되며 스트림은 메시지로 종료됩니다.
   - stop: API가 추가 토큰 생성을 중지하는 최대 4개의 시퀀스입니다.
   - max_tokens: 채팅 완료 시 생성할 최대 토큰 수입니다.

   입력 토큰과 생성된 토큰의 총 길이는 모델의 컨텍스트 길이에 의해 제한됩니다.
   - presence_penalty: -2.0에서 2.0 사이의 숫자입니다. 양수 값은 지금까지 텍스트에 나타나는지 여부에 따라 새 토큰에 불이익을 주어 모델이 새로운 주제에 대해 이야기할 가능성을 높입니다.
   - frequency_penalty: -2.0에서 2.0 사이의 숫자입니다. 양수 값은 지금까지 텍스트의 기존 빈도에 따라 새 토큰에 불이익을 주어 모델이 동일한 줄을 그대로 반복할 가능성을 줄입니다.
   - logit_bias: 지정된 토큰이 완료에 나타날 가능성을 수정합니다.

   토큰(토크나이저의 토큰 ID로 지정됨)을 -100에서 100 사이의 연결된 바이어스 값에 매핑하는 json 개체를 허용합니다. 수학적으로 편향은 샘플링 전에 모델에 의해 생성된 로짓에 추가됩니다. 정확한 효과는 모델마다 다르지만 -1과 1 사이의 값은 선택 가능성을 줄이거나 증가시켜야 합니다. -100 또는 100과 같은 값은 관련 토큰의 금지 또는 배타적 선택을 초래해야 합니다.
   - user: OpenAI가 남용을 모니터링하고 감지하는 데 도움이 될 수 있는 최종 사용자를 나타내는 고유 식별자입니다.

### model
사용 가능한 모델의 목록은 다음과 같다.

   gpt-4, 
   gpt-4-0613, 
   gpt-4-32k, 
   gpt-4-32k-0613, 
   gpt-3.5-turbo, 
   gpt-3.5-turbo-0613, 
   gpt-3.5-turbo-16k, 
   gpt-3.5-turbo-16k-0613

   <!-- text-davinci-003, 
   text-davinci-002, 
   text-davinci-001, 
   text-curie-001, 
   text-babbage-001, 
   text-ada-001, 
   davinci, 
   curie, 
   babbage, 
   ada

   whisper-1

   davinci, 
   curie, 
   babbage, 
   
   ada

   text-embedding-ada-002,
   text-similarity-*-001, 
   text-search-*-*-001, 
   code-search-*-*-001

   text-moderation-stable, 
   text-moderation-latest -->


2. playground에서 테스트 해 볼 수 있다.
- https://platform.openai.com/playground?mode=chat 