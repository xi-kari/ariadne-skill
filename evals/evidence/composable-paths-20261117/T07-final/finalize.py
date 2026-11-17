import hashlib
import json
from pathlib import Path

task_dir = Path.cwd()
task = task_dir.name
skill_dir = '/workspace/ariadne-behavior-runs/skill-final'

def event(number, kind, command, cwd, result):
    return {'session_operation_id': number, 'kind': kind, 'command': command,
            'cwd': cwd, 'exit_code': 0, 'result': result}

events = [
    event(1, 'read', 'cat /workspace/ariadne-behavior-runs/skill-final/SKILL.md',
          '/workspace', '已读取冻结技能入口。'),
    event(2, 'read', 'cat prompt.txt', str(task_dir),
          '已读取本任务的合成案例请求；未将其视为现实观测。'),
    event(3, 'read', 'cat /workspace/ariadne-behavior-runs/skill-final/references/kernel.md',
          '/workspace', '已读取 Kernel。'),
    event(4, 'read', 'cat paths/understand.md paths/project.md references/library/evidence-contracts.md references/library/representation-and-closure.md',
          skill_dir, '工具输出发生截断；实际看到 Understand、Project 大部分内容、Representation and Closure，以及 Evidence 的部分内容。后续对需要的缺口进行了定向读取。'),
    event(5, 'read', 'cat references/responsibility.md', skill_dir,
          '已读取责任、证据身份与结论依赖的说明。'),
    event(6, 'read', "rg -n 'total|causal|mechanism|effect|^##' references/library/evidence-contracts.md", skill_dir,
          '已检索因果效应、机制、整体效应与证据依赖相关行。'),
    event(7, 'read', 'tail -n 12 paths/project.md', skill_dir,
          '已读取 Project 尾部的失效边界与停止条件。'),
    event(8, 'read', "sed -n '56,72p;95,108p' references/library/evidence-contracts.md", skill_dir,
          '已读取证据链及局部效应与整体效应的相关完整段落。'),
]

if task == 'T02-final':
    calculation = "python - <<'PY'\nfrom fractions import Fraction\nrows=[(1,1,Fraction(2,10)),(1,0,Fraction(3,10)),(0,1,Fraction(3,10)),(0,0,Fraction(2,10))]\nfirst=sum(u*p for u,v,p in rows)\nsecond=sum(v*p for u,v,p in rows)\ntotal=sum(u*v*p for u,v,p in rows)\nprint({'first_edge':str(first),'second_edge':str(second),'chain_total':str(total),'product_of_means':str(first*second),'covariance':str(total-first*second)})\nassert (first,second,total)==(Fraction(1,2),Fraction(1,2),Fraction(1,5))\nPY"
    output = {'first_edge': '1/2', 'second_edge': '1/2', 'chain_total': '1/5', 'product_of_means': '1/4', 'covariance': '-1/20'}
else:
    calculation = "python - <<'PY'\nq=80\ntrajectory=[q]\nfor day in range(7):\n    q+=5-4\n    trajectory.append(q)\nprint({'trajectory':trajectory,'day_7':q,'exceeds_100':q>100,'minimum_integer_net_addition_for_over_100':21,'maximum_completions_for_over_100_with_35_arrivals':14})\nassert q==87\nassert 80+35-14>100 and 80+35-15==100\nPY"
    output = {'trajectory': [80,81,82,83,84,85,86,87], 'day_7': 87, 'exceeds_100': False, 'minimum_integer_net_addition_for_over_100': 21, 'maximum_completions_for_over_100_with_35_arrivals': 14}
events.append(event(9, 'calculate', calculation, str(task_dir), output))
events.append({'session_operation_id': 10, 'kind': 'write', 'tool': 'apply_patch',
               'path': str(task_dir / 'response.md'),
               'result': '工具实际新增了中文回答；返回 {}。没有修改冻结技能。'})
events.append(event(11, 'read', 'cat response.md', str(task_dir),
                    '已完整读回初稿；发现行内数学定界符缺失起始反斜杠，T02 另有多余加号。'))
events.append({'session_operation_id': 12, 'kind': 'read_write', 'tool': 'exec_command',
               'cwd': '/workspace/ariadne-behavior-runs/T02-final',
               'command': "python - <<'PY'\nfrom pathlib import Path\nimport re\nfor task in ['T02-final','T07-final']:\n    p=Path('/workspace/ariadne-behavior-runs')/task/'response.md'\n    s=p.read_text()\n    s,n=re.subn(r'(?<!\\\\)\\(([^()\\n]+)\\\\\\)',lambda m:'\\\\('+m.group(1)+'\\\\)',s)\n    s=s.replace('整体效应为：+\\n','整体效应为：\\n\\n')\n    p.write_text(s)\n    print(task, 'inline_math_delimiters_fixed', n, 'characters', len(s))\nPY",
               'exit_code': 0, 'stdout': 'T02-final inline_math_delimiters_fixed 19 characters 1416\nT07-final inline_math_delimiters_fixed 2 characters 765\n'})

response_path = task_dir / 'response.md'
response = response_path.read_text()
assert response.count('\\(') == response.count('\\)')
assert response.count('\\[') == response.count('\\]')
assert '整体效应为：+' not in response
digest = hashlib.sha256(response.encode()).hexdigest()
events.append(event(13, 'read_check', 'python finalize.py', str(task_dir),
                    {'response_characters': len(response), 'response_sha256': digest,
                     'inline_math_pairs': response.count('\\('),
                     'display_math_pairs': response.count('\\['),
                     'delimiter_checks_passed': True}))
record = {'task': task, 'case_status': 'synthetic',
          'record_scope': '本任务相关实际操作。相同 session_operation_id 的共享技能读取仅执行过一次，并在两个任务日志中重复引用。文字结果为实际输出的摘要，不表示完整输出逐字存档。',
          'operations': events,
          'log_write': {'command': 'python finalize.py', 'path': str(task_dir / 'execution.json')}}
log_path = task_dir / 'execution.json'
log_path.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
parsed = json.loads(log_path.read_text())
assert parsed['operations'][-1]['result']['response_sha256'] == digest
print(json.dumps({'task': task, 'response_characters': len(response),
                  'response_sha256': digest, 'execution_json_parses': True}, ensure_ascii=False))
print(response)
