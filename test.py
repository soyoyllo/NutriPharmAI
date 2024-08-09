import gradio as gr

# def


_HEADER_ = '''
<h2><b>💊 Pill_assistant: 약물 보조 AI 💊 </b></h2><h2>
키, 몸무게, 성별, 복용 약물을 입력해 권장 복용량을 추천해줍니다!
'''

with gr.Blocks(title="pill assistant") as demo:
    gr.Markdown(_HEADER_)
    with gr.Column():
        fill_select = gr.Radio(["의약품", "영양보조제"], label="의약품 or 영양제", info='확인하고자 하는 복용제를 선택하여 주세요!')
        tall = gr.Textbox(label="키(신장)", placeholder='당신의 키(신장)를 넣어주세요!')
        weight = gr.Textbox(label="몸무게", placeholder='당신의 몸무게를 넣어주세요!')
        sex = gr.Radio(["남성", "여성"], label="성별", info='당신의 성별을 선택해주세요!')
        if fill_select == '의약품':
            fill = gr.Dropdown(
                ["타이레놀", "판콜", "스트렙실"], multiselect=True, label="약품",
                info="복용 중인 약품을 선택하여 주세요!"
            )
        else:
            fill = gr.Dropdown(
                ["락포핏", "얼라이브종합비타민", "밀크시슬"], multiselect=True, label="영양제", info="복용 중인 영양제를 선택하여 주세요!"
            )
        submit = gr.Button("생성하기")

    with gr.Row():
        output = gr.Textbox(label="권장 복용 설명")
        # quest_item_img = gr.Image(label='퀘스트 아이템', elem_id='quest_item')

    # submit.click(fn=call_model, inputs=[tall, weight, sex, fill], outputs=[output, quest_item_img])

demo.launch(share=True)