< GIT이 관리하는 3가지 영역 >

- Working Directory = 작업영역
: 사용자의 작업이 이루어지는 곳 (바탕화면 git_test폴더)
- Staging Area ( = Index)
:  커밋을 위한 파일, 폴더가 추가되는 곳 / 거치는 중간영역 / 가상의 공간이다.
- Repository
: staging area 에 있던 파일 및 폴더의 변경사항을 저장하는 곳

Working Directory => Staging Area => Repository 의 과정으로 버전관리를 수행합니다.



git init 입력
- 현재 작업중인 디렉토리를 Git 으로 관리한다는 명령어
- .git 이라는 숨김 폴더를 생성하고, 터미널에는 master라고 표기됩니다.


!! 주의사항 !!
1. 이미 Git으로 관리되고 있는 (Git 저장소인) 폴더 안에서 또다른 Git 저장소를 만들지 않도록 주의합니다! (=중첩 금지) => 터미널에 이미 (master) 가 표시되어 있다면 git init 라는 명령어를 입력하지 않는다.
2. 절대로 홈디렉토리에서  git init을 입력하지 않는다. (터미널의 경로가 ~인지 확인합니다.)


git status 입력
 - Working Directory 와 Staging Area에 있는 파일의 현재 상태를 알려주는 명령어
- 어떤 작업을 시행하기 전에 수시로 status로 현재 상태를 확인하면 좋습니다.


파일의 상태??

1. Untracked : Git이 관리하지 않는 파일(한번도 Staging Area에 올라간적이 없는 파일)
2. Tracked : Git이 관리하는 파일
 | 1. Unmodified : 최신상태
 | 2. Modified : 수정되었지만 아직 Staging Area 에는 올라가지 않은 상태
 | 3. Staged : Staging Area 에 올라간 상태


touch a.txt b.txt  ( touch : 파일 생성하는 명령어)  ------ 1. Untracked (Git이 관리하지 않는 파일)


git add

- Working Directory에 있는 파일을 Staging Area로 올리는 명령어
- Git 이 해당 파일을 추적(관리) 할 수 있도록 만든다.
- Untracked, Modified => Staged 로 상태를 변경한다.

git add a.txt ----- 2. Tracked (Git이 관리하는 파일)

파일 하나만 올리기 : git add 파일이름

폴더 올리기 : git add 폴더이름

현재 디렉토리에 속한 파일/폴더 전부 : git add .     ----- "가장 많이 사용하는 명령어" 


 2교시

...
git commit
...
- Staging Area 에 올라온 파일의 변경사항을 하나의 버전(커밋)으로 저장하는 명령어
- 커밋 메시지는 현재 변경사항들을 잘 나타낼 수 있도록 의미있게 작성하는 것을 권장합니다.
- 각각의 커밋은 sha-1 알고리즘에 의해 반환된 고유의 해시값을 ID(중복x)로 가진다.
- root commit 은 해당 커밋이 최초의 커밋일 때만 표시된다.

...
git commit -m "커밋메시지"
...



...
git log
...
- 커밋 내역(ID, 작성자, 시간 , 메시지)를 조회할 수 있는 명령어
- 옵션
    - ``` --online``` : 한줄로 축약해서 보여준다.
    - ``` --graph``` : 브랜치와 머지 내역을 그래프로 보여준다.

  ## 원격 저장소에 업로드

- 파일을 Github 원격 저장소에 업로드
- 정확히 말하면, 파일을 업로드하는게 아니라, 커밋 내역을 업로드 하는것
- 로컬 저장소에서 커밋을 생성해야 원격 저장소에 업로드 할 수 있다.

...
git push
...
- 로컬저장소 커밋을 원격 저장소에 업로드 하는 명령어
- ```git push 저장소이름 브랜치이름```형식으로 작성합니다.
- ```-u``` 옵션을 사용하면, 두번째 커밋부터는 저장소이름과 브랜치이름 생략 가능



## 원격 저장소 가져오기

...
git clone
...
- 원격 저장소의 커밋 내역을 모두 가져와서, 로컬 저장소를 생성하는 명령어
- clone "복제" 라는 뜻으로, ```git clone``` 명령어를 사용하면 원격 저장소를 통째로 복제해서 내 컴퓨터에 옮길 수 있다.
...
git clone 원격저장소주소
...
- git clone을 통해 생성된 로컬저장소는 git init, git remote add 가 이미 수행되어 있습니다.


...
git pull
...
- 원격 저장소의 변경 사항을 가져와서, 로컬 저장소를 업데이트 하는 명령어
- 로컬 저장소와 원격 저장소의 내용이 완전 일치하면, git pull 을 해도 아무런 변화가 일어나지 않습니다.
...
git pull 저장소이름 브랜치이름
....
git pull origin master
...
