package com.appnap.frontend;

import android.content.Intent;
import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.design.widget.BottomNavigationView;
import android.support.v7.app.AppCompatActivity;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.appnap.frontend.handler.HTTPRequestSingleton;

import java.util.HashMap;
import java.util.Map;

public class MainActivity extends AppCompatActivity {

    private TextView mTextMessage;
    private Button mLoginLaunchActivity;
    private RequestQueue mQueue;

    private BottomNavigationView.OnNavigationItemSelectedListener mOnNavigationItemSelectedListener
            = new BottomNavigationView.OnNavigationItemSelectedListener() {

        @Override
        public boolean onNavigationItemSelected(@NonNull MenuItem item) {
            switch (item.getItemId()) {
                case R.id.navigation_home:
                    mTextMessage.setText(R.string.server_url);
                    return true;
                case R.id.navigation_dashboard:
                    mTextMessage.setText(R.string.title_dashboard);
                    return true;
                case R.id.navigation_notifications:
                    mTextMessage.setText(R.string.title_notifications);
                    return true;
            }
            return false;
        }
    };

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        mTextMessage = (TextView) findViewById(R.id.message);
        BottomNavigationView navigation = (BottomNavigationView) findViewById(R.id.navigation);
        navigation.setOnNavigationItemSelectedListener(mOnNavigationItemSelectedListener);

        mLoginLaunchActivity = (Button) findViewById(R.id.login_launch_activity);
        mLoginLaunchActivity.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View view){
                launchActivity();
            }
        });

        mQueue = HTTPRequestSingleton.getInstance(this.getApplicationContext()).
            getRequestQueue();
        UpdateUsername();
    }

    private void launchActivity() {
        Intent intent = new Intent(this, LoginActivity.class);
        startActivityForResult(intent, ResultCode.USERLOGIN.ordinal());
    }

    @Override
    protected void onActivityResult (int requestCode, int resultCode, Intent data){
        // Do whatever you would like to do

        if (requestCode == resultCode && resultCode == ResultCode.USERLOGIN.ordinal())
        {
            UpdateUsername();
            mLoginLaunchActivity.setVisibility(View.GONE);
        }
        if (requestCode == resultCode && resultCode == ResultCode.USERLOGOUT.ordinal())
        {
            UpdateUsername();
            mLoginLaunchActivity.setVisibility(View.VISIBLE);
        }
    }

    private void UpdateUsername(){

        final TextView mTextView = (TextView) findViewById(R.id.message);

        // Request a string response from the provided URL.
        StringRequest stringRequest = new StringRequest(Request.Method.GET,
                getResources().getString(R.string.server_url) + "/userLogged",
                new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {
                        // Display the first 500 characters of the response string.
                        mTextView.setText("User logged is: "+ response);
                    }
                }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                mTextView.setText("That didn't work!");
            }
        })
        {
            @Override
            public Map<String, String> getHeaders() {
                Map<String, String> params = new HashMap<String, String>();
                params.put("api_username", HTTPRequestSingleton.getInstance(getApplicationContext()).getUsername());
                params.put("api_access_token", HTTPRequestSingleton.getInstance(getApplicationContext()).getToken());
                return params;
            }
        };

        // Add the request to the RequestQueue.
        mQueue.add(stringRequest);
    }

}
