# 3D印刷したいデザインのリストを作成する
unprinted_designs = ['iPhoneケース', 'ロボットのペンダント', '12面体']
completed_models = []

# リストからなくなるまでデザインを3D印刷する
#  各デザインは印刷後に completed_models に移動する
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"3D印刷中: {current_design}")
    completed_models.append(current_design)

# 3D印刷が完了したモデルを出力する
print("\n以下のモデルが3D印刷されました")
for completed_model in completed_models:
    print(completed_model)
