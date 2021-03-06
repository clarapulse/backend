from db import *
from faker import Faker
import uuid
import random

hs = []

univ = [
    "Academy of Art College",
    "Adams State College",
    "Adelphi University",
    "Adler School of Professional Psychology",
    "Adrian College",
    "Agnes Scott College",
    "Air Force Institute of Technology",
    "Alabama Agricultural and Mechanical University",
    "Alabama State University",
    "Alaska Bible College",
    "Alaska Pacific University",
    "Albany College of Pharmacy",
    "Albany Law School",
    "Albany Medical Center",
    "Albany State University",
    "Albertus Magnus College",
    "Albion College",
    "Albright College",
    "Alcorn State University",
    "Alderson Broaddus College",
    "Alfred Adler Graduate School",
    "Alfred University",
    "Alice Lloyd College",
    "Allegheny College",
    "Allen University",
    "Alma College",
    "Alvernia College",
    "Alverno College",
    "Ambassador University",
    "Amber University",
    "American Academy of Nutrition",
    "American Business & Technology University",
    "American Conservatory of Music",
    "American Conservatory Theater",
    "American-European School of Management ",
    "American Film Institute Center for Advanced Film and Television Studies",
    "American Indian College",
    "American InterContinental University - Atlanta",
    "American InterContinental University - Ft. Lauderdale",
    "American InterContinental University - Georgia",
    "American InterContinental University Online",
    "American International College",
    "American Jewish University",
    "American Military University",
    "American Public University",
    "American University",
    "American World University",
    "Amherst College",
    "Anderson College",
    "Anderson University",
    "Andon College - Modesto",
    "Andon College - Stockton",
    "Andrew Jackson University",
    "Andrews University",
    "Angelo State University",
    "Anna Maria College",
    "Antioch New England Graduate School",
    "Antioch University",
    "Antioch University Los Angeles",
    "Antioch University Santa Barbara",
    "Antioch University Seattle",
    "Appalachian Bible College",
    "Appalachian State University",
    "Aquinas College",
    "Arcadia University",
    "Argosy University",
    "Argosy University - Hawaii",
    "Arizona Christian University",
    "State University",
    "Arizona State University",
    "Arizona State University",
    "Arizona State University",
    "Arizona State University",
    "Arkansas State University",
    "Arkansas State University",
    "Arkansas State University",
    "Arkansas State University",
    "Arkansas Tech University",
    "Arlington Baptist College",
    "Armstrong Atlantic State University",
    "Armstrong University",
    "Art Academy of Cincinnati",
    "Art Center College of Design",
    "Arthur D. Little Management Education Institute",
    "Art Institute of Charlotte",
    "Art Institute of Southern California",
    "Asbury College",
    "Ashland University",
    "Assumption College",
    "Athenaeum of Ohio",
    "Athens State College",
    "Atlanta Christian College",
    "Atlanta College of Art",
    "Atlantic International University",
    "Atlantic Union College",
    "Atlantic University",
    "Auburn University",
    "Auburn University at Montgomery",
    "Audrey Cohen College",
    "Augsburg College",
    "Augustana College",
    "Augustana College",
    "Augusta State University",
    "Aurora University",
    "Austin College",
    "Austin Community College",
    "Austin Peay State University",
    "Ave Maria University",
    "Benedict College",
    "Benedictine College",
    "Benedictine University",
    "Benedictine University",
    "Bennett College",
    "Bennington College",
    "Bentley College",
    "Berea College",
    "Berean University of the Assemblies of God",
    "Berklee College of Music",
    "Berne University",
    "Berry College",
    "Bethany College California",
    "Bethany College Kansas",
    "Bethany College West Virginia",
    "Cabrini College",
    "Caldwell College",
    "California Baptist College",
    "California Coast University",
    "California College for Health Sciences",
    "California College of Arts and Crafts",
    "Colorado Technical University",
    "Columbia College Chicago",
    "Columbia College Hollywood",
    "Columbia College of Missouri",
    "Columbia College South Carolina",
    "Columbia Commonwealth University",
    "Columbia International University",
    "Columbia Southern University",
    "Columbia Union College",
    "Columbia University",
    "Columbus College of Art and Design",
    "Columbus State University",
    "Columbus University",
    "Community College of Denver",
    "Goddard College",
    "God's Bible School and College",
    "Golden Gate University",
    "Goldey-Beacom College",
    "Gonzaga University",
    "Gordon College",
    "Gordon Conwell Theological Seminary",
    "Goshen College",
    "Goucher College",
    "Governors State University",
    "Grace Bible College",
    "Grace College",
    "Graceland College",
    "Grace University",
    "Graduate Theological Union",
    "Grambling State University",
    "Grand Canyon University",
    "Grand Valley State University",
    "Grand View College",
    "Grantham University",
    "Gratz College",
    "Great Lakes Christian College",
    "Green Mountain College",
    "Greensboro College",
    "Greenville College",
    "Grinnell College",
    "Grove City College",
    "Guilford College",
    "Gustavus Adolphus College",
    "Gwynedd-Mercy College",
    "Jackson State University",
    "Jacksonville State University",
    "Jacksonville University",
    "James Madison University",
    "Jamestown College",
    "Jarvis Christian College",
    "John Brown University",
    "John Carroll University",
    "John F. Kennedy University",
    "John Marshall Law School",
    "John Paul the Great Catholic University",
    "Johns Hopkins University",
    "Johnson Bible College",
    "Johnson County Community College",
    "Johnson C. Smith University",
    "Lancaster Bible College",
    "Lander University",
    "Lane College",
    "Langston University",
    "La Roche College",
    "La Salle University",
    "Lasell College",
    "La Sierra University",
    "Laurus Technical Institute",
    "Lawrence Technological University",
    "Lawrence University",
    "Lebanon Valley College",
    "Lees-McRae College",
    "Lee University",
    "Lehigh Univervsity",
    "Le Moyne College",
    "Le Moyne-Owen College",
    "Stephen F. Austin State University",
    "Stephens College",
    "Sterling College",
    "Stetson University",
    "Stevens Institute of Technology",
    "The Johns Hopkins University",
    "The Juilliard School",
    "The Leadership Institute of Seattle",
    "The Maryland Institute",
    "The Master's College",
    "The McGregor School of Antioch University",
    "The Naropa Institute",
    "The New School",
    "The Rockefeller University",
    "The School of the Art Institute of Chicago",
    "The Scripps Research Institute",
    "The Southern Christian University",
    "The Tulane University of New Orleans",
    "The Union Institute",
    "Thiel College",
    "Thomas A. Edison State College",
    "Thomas Aquinas College",
    "Thomas College Maine",
    "Thomas Jefferson University",
    "Thomas More College",
    "Thomas More College of Liberal Arts",
    "Thomas University",
    "Thunderbird School of Global Management",
    "Tiffin University",
    "Toccoa Falls College",
    "Tomball College",
    "Tougaloo College",
    "Touro College",
    "Touro University",
    "Towson University",
    "Transylvania University",
    "Trevecca Nazarene University",
    "Tri-College University",
]
hs = [
    "South Fork High School",
    "Mammoth Kindergarten High School",
    "Oakwood College High School",
    "Crystal River High School",
    "Oakleaf School High School",
    "Saint Mary's High School",
    "Grand Mountain High School",
    "Grand Mountain High School",
    "Acadia Institute High School",
    "Pinewood Academy High School",
    "Horizon Elementary High School",
    "Sunny Coast High School",
    "Whale Gulch High School",
    "Martin Luther High School",
    "Saint Helena High School",
    "Summers Academy High School",
    "Central Valley High School",
    "Deer Valley High School",
    "Southview High High School",
    "Westside College High School",
    "Silver Valley High School",
    "Lakewood High High School",
    "Somerset School High School",
    "Canyon View High School",
    "Lakewood Elementary High School",
    "River Valley High School",
    "Spring Gardens High School",
    "Oak Ridge High School",
    "Willow Technical High School",
    "Pioneer College High School",
]
# create dumb ass users
CDB.drop_tables([User, Intention, Connection])
CDB.create_tables([User, Intention, Connection])
x = []
intent = 1
dataUser = []
dataIntent = []
for i in range(6):
    fake = Faker()
    _x = uuid.uuid4()
    x.append(_x)
    dataUser.append(
        {
            "user_id": _x,
            "name": fake.name(),
            "email": f"shou+{i}@ucsb.edu",
            "url": f"https://picsum.photos/60/60?random={i}",
            "is_highschool": i % 2 == 1,
            "highschool": random.choice(hs) if i % 2 == 1 else None,
            "university": random.choice(univ) if i % 2 != 1 else None,
        }
    )

    if i % 2 == 1:
        for j in range(0, random.randint(2, 10)):
            intent += 1
            dataIntent.append(
                {
                    "intention_id": intent,
                    "user_id": _x,
                    "univ_name": random.choice(univ),
                }
            )
print("done loading")
User.insert_many(dataUser).execute()
Intention.insert_many(dataIntent).execute()
print("done 1/2")
conn = 1
connData = []
done = ""
for i in range(0):
    try:
        conn += 1
        w1 = random.choice(x)
        w2 = random.choice(x)
        if str(w1) + str(w2) in done or str(w2) + str(w1) in done:
            continue
        done += str(w1) + str(w2)
        connData.append({"connection_id": conn, "user_id_one": w1, "user_id_two": w2})
    except Exception as e:
        print(e)
Connection.insert_many(connData).execute()
